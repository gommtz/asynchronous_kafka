"""Utility functions module."""
# Python libraries
from uuid import uuid4


def gen_uuid() -> str:
    """Generate a uuid4 string."""

    return str(uuid4())
