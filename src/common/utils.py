"""Utility functions module."""

import sys
import logging

# Python libraries
from uuid import uuid4

# Logger init and logger format
sys_logger = logging.getLogger("")
sys_logger.setLevel(logging.INFO)
format_str = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# Stream handler
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(format_str)
sys_logger.addHandler(handler)


class Logger:
    """Custom logger to always get instant flushes."""

    def info(self, message):
        sys_logger.info(message)
        handler.flush()

    def error(self, message):
        sys_logger.error(message)
        handler.flush()

    def debug(self, message):
        sys_logger.debug(message)
        handler.flush()


logger = Logger()

def gen_uuid() -> str:
    """Generate a uuid4 string."""

    return str(uuid4())
