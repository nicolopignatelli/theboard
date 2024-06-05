import os
import logging
import logging.config

from colorama import Fore, Style, init as init_colorama

# Default config for autogen agents
LLM_CONFIG = {"config_list": [{"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"]}]}

# Logging configuration
init_colorama(autoreset=True)


class ColoredFormatter(logging.Formatter):
    # Define colors for each log level
    COLORS = {
        'DEBUG': Fore.BLUE,
        'INFO': Fore.GREEN,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.MAGENTA,
    }

    def format(self, record):
        log_color = self.COLORS.get(record.levelname, Fore.WHITE)
        message = super().format(record)
        return f"{log_color}{message}{Style.RESET_ALL}"


def setup_logging():
    logging_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            },
            'colored': {
                '()': ColoredFormatter,
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'colored',
                'level': 'INFO',
            },
            'file': {
                'class': 'logging.FileHandler',
                'formatter': 'standard',
                'level': 'DEBUG',
                'filename': 'app.log',
            },
        },
        'root': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        }
    }

    logging.config.dictConfig(logging_config)
