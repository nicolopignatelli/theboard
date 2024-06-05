import uuid
from pydantic import BaseModel
from typing import TypeAlias, Dict, Callable, Any, Literal, TypedDict


class Envelope(TypedDict):
    type: str
    data: dict[str, Any]


class Message(BaseModel):
    def type(self) -> str:
        return self.__class__.__name__

    def envelope(self) -> Envelope:
        return {"type": self.type(), "data": self.model_dump(mode="json")}


class FlushQueue(Message):
    pass

Topic: TypeAlias = str
SubscriberId: TypeAlias = str
Handler: TypeAlias = Callable[[Message], None]
Subscribers: TypeAlias = Dict[SubscriberId, Callable]

subscriptions: Dict[Topic, Subscribers] = {}


def subscribe(topic: Topic, handler: Handler) -> SubscriberId:
    if topic not in subscriptions:
        subscriptions[topic] = {}

    subscriber_id: SubscriberId = str(uuid.uuid4())
    subscriptions[topic][subscriber_id] = handler

    return subscriber_id


def unsubscribe(subscriber_id: SubscriberId, topic: Topic) -> None:
    if topic not in subscriptions or subscriber_id not in subscriptions[topic]:
        return

    subscriptions[topic].pop(subscriber_id)


def publish(topic, message: Message) -> None:
    if topic in subscriptions:
        for handler in subscriptions[topic].values():
            handler(message)
