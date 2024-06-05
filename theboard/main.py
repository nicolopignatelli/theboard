import asyncio
import logging
import uuid
from queue import Queue
from typing import Any, Dict, TypeAlias

import uvicorn
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from starlette.websockets import WebSocketState

from theboard import messages, pubsub
from theboard.board.build import build_the_board
from theboard.config import setup_logging

from fastapi import FastAPI, Request, WebSocket

from theboard.discussion import DiscussionForum, SelectTheMostRelevant
from theboard.pubsub import Message, FlushQueue, Envelope

setup_logging()
app = FastAPI()
templates = Jinja2Templates(directory="templates")
the_board = build_the_board()

SessionId: TypeAlias = str
sessions_messages_queues: Dict[SessionId, Queue] = {}
sessions_websockets: Dict[SessionId, WebSocket] = {}


async def process_session_message_queue(session_id: SessionId):
    async def send_data(data: dict[str, Any]):
        websocket = await asyncio.to_thread(sessions_websockets.get, session_id)

        if (websocket is None) or (not (
                websocket.application_state == WebSocketState.CONNECTED and websocket.client_state == WebSocketState.CONNECTED
        )):
            return

        await websocket.send_json(data)

    flush_queue = False
    queue: Queue = await asyncio.to_thread(sessions_messages_queues.get, session_id)

    while not flush_queue:
        try:
            envelope: Envelope = await asyncio.to_thread(queue.get)
            if envelope["type"] == FlushQueue().type():
                flush_queue = True
                break
            else:
                await send_data(envelope)
        except Exception as e:
            logging.error(f"Error sending websocket message: {e}")

    while not await asyncio.to_thread(queue.empty):
        envelope = await asyncio.to_thread(queue.get)
        await send_data(envelope)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    session_id = str(uuid.uuid4())
    sessions_websockets[session_id] = websocket
    sessions_messages_queues[session_id] = Queue()

    def handle_message(message: Message):
        envelope = message.envelope()
        sessions_messages_queues[session_id].put(envelope)

    listener_id = pubsub.subscribe(session_id, handle_message)

    async def process_matter(matter: str):
        members_selection_method = SelectTheMostRelevant(the_board=the_board)
        discussion_forum = DiscussionForum(
            _discussion_forum_id=session_id,
            _members_selection_method=members_selection_method,
            _matter=matter,
        )

        discussion_forum_started = messages.DiscussionForumStarted(
            discussion_forum_id=session_id,
            member_selection_method_name=str(members_selection_method),
        )
        pubsub.publish(session_id, discussion_forum_started)

        await asyncio.to_thread(discussion_forum.discuss)
        sessions_messages_queues[session_id].put(FlushQueue().envelope())

    try:
        matter = await websocket.receive_text()

        await asyncio.gather(
            process_matter(matter),
            process_session_message_queue(session_id)
        )
    except Exception as e:
        logging.error(f"Error in websocket endpoint: {e}")
    finally:
        pubsub.unsubscribe(listener_id, session_id)
        await websocket.close()
        del sessions_websockets[session_id]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
