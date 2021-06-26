import asyncio
from typing import Any, Dict

from .events import EventBase


class Client(EventBase):
    """Manages a connection to Pyfinity hub."""

    def __init__(self, ws_url: str, aiohttp_session):
        self.ws_url = ws_url
        self.aiohttp_session = aiohttp_session

    async def connect(self) -> None:
        """Connects to the pyfinity hub."""
        raise NotImplementedError

    async def listen(self, driver_ready: asyncio.Event) -> None:
        """Start listening to the websocket."""
        raise NotImplementedError

    async def getState(self) -> Dict[str, Any]:
        raise NotImplementedError