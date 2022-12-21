import logging.config
import logging
import typing
import os

_default = ""


def _env_str(key: str, default: typing.Any = _default) -> str:
    key = key.strip()
    result = os.getenv(key)

    if result:
        return result.strip()

    if default is not _default:
        return default

    raise ValueError("Configuration value for {0} not set!".format(key))


def _env_bool(key: str, default: bool = False) -> bool:
    r = _env_str(key, -1)
    if r == -1:
        return default

    return int(r) != 0


def _env_int(key: str, default: int) -> int:
    return int(_env_str(key, default))


class Settings:
    def __init__(self):
        self.PORT = _env_int("PORT", 8000)
        self.KAFKA_BOOTSTRAP_SERVERS = _env_str(
            "KAFKA_BOOTSTRAP_SERVERS", "localhost:29092"
        )
        self.KAFKA_CONSUMER_GROUP_PREFIX = _env_str(
            "KAFKA_CONSUMER_GROUP_PREFIX", "group"
        )
        self.KAFKA_TOPIC = _env_str("KAFKA_TOPIC")


# Global variable to import settings
settings = Settings()
