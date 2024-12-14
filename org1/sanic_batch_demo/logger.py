import logging
import os
import sys
from typing import Dict, Any
from pathlib import Path
from loguru import logger

APP_NAME = "sqlglot_service"

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")

HOST_NAME = os.environ.get("POD_IP", "UNKNOWN")

if LOG_LEVEL == "DEBUG":
    print(f"log level is {LOG_LEVEL}, setting log path to ./logs/{APP_NAME}")
    APP_LOG_PATH = Path(f"./logs/{APP_NAME}")
else:
    APP_LOG_PATH = Path(f"/cz/logs/{APP_NAME}")

APP_LOG_PATH.mkdir(parents=True, exist_ok=True)

LOG_FORMAT = (
        "{time:YYYY-MM-dd HH:mm:ss} |<lvl>{level:1}</>|"
        + "[{thread.name}] "
        + "{name}:{line:1} - "
        + "<lvl>{message}</>"
)

logger.remove()

logger.add(
    sys.stdout,
    format=LOG_FORMAT,
    level="WARNING",
    backtrace=True,
    diagnose=False,
    colorize=True if LOG_LEVEL == "DEBUG" else False,
)

logger.add(
    APP_LOG_PATH / f"info.{APP_NAME}-{HOST_NAME}.log.{{time:YYYY-MM-DD}}.log",
    format=LOG_FORMAT,
    level="INFO",
    rotation="100 MB",
    retention="1 months",
    encoding="utf-8",
    colorize=False,
)

logger.add(
    APP_LOG_PATH / f"error.{APP_NAME}-{HOST_NAME}.log.{{time:YYYY-MM-DD}}.log",
    format=LOG_FORMAT,
    level="ERROR",
    rotation="100 MB",
    retention="1 months",
    encoding="utf-8",
    filter=lambda record: record["level"].name == "ERROR",
    colorize=False
)

logger.add(
    APP_LOG_PATH / f"warn.{APP_NAME}-{HOST_NAME}.log.{{time:YYYY-MM-DD}}.log",
    format=LOG_FORMAT,
    level="WARNING",
    rotation="100 MB",
    retention="1 months",
    encoding="utf-8",
    filter=lambda record: record["level"].name == "WARNING",
    colorize=False
)

logger.add(
    APP_LOG_PATH / f"debug.{APP_NAME}-{HOST_NAME}.log.{{time:YYYY-MM-DD}}.log",
    format=LOG_FORMAT,
    level="DEBUG",
    rotation="100 MB",
    retention="10 days",
    encoding="utf-8",
    filter=lambda record: record["level"].name == "DEBUG",
    colorize=False
)

S_LOGGING_CONFIG_DEFAULTS: Dict[str, Any] = dict(  # no cov
    version=1,
    disable_existing_loggers=False,
    datefmt='%Y-%M-%D %H:%M:%S',
    loggers={
        "sanic.root": {"level": "INFO", "handlers": ["console"], "propagate": False},
        "sanic.error": {
            "level": "INFO",
            "handlers": ["error_console"],
            "propagate": False,
            "qualname": "sanic.error",
        },
        "sanic.access": {
            "level": "INFO",
            "handlers": ["access_console"],
            "propagate": False,
            "qualname": "sanic.access",
        },
        "sanic.server": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False,
            "qualname": "sanic.server",
        },
    },
    handlers={
        "console": {
            "class": "logger.InterceptHandler",
        },
        "error_console": {
            "class": "logger.InterceptHandler",
        },
        "access_console": {
            "class": "logger.InterceptHandler",
        },
    }
)


class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno
        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def setup_log():
    logging.root.handlers = [InterceptHandler()]
    logging.root.setLevel(LOG_LEVEL)
    for name in logging.root.manager.loggerDict.keys():
        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True
