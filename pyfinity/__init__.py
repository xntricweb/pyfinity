# main pyfinity module
import asyncio
from dataclasses import dataclass
from typing import Any, Dict
import aiohttp

from .client import Client


class BasePyfinityError(Exception):
    """Base Pyfinity exception."""


@dataclass
class VersionInfo:
    hub_id: str
    hub_version: str

    @classmethod
    def from_message(cls, msg: dict) -> "VersionInfo":
        """Create a version info from a version message."""
        return cls(hub_id=msg["hubId"], hub_version=msg["hubVersion"])


async def get_server_version(url: str, session: aiohttp.ClientSession) -> VersionInfo:
    """Return the pyfinity version data"""
    client = await session.ws_connect(url)
    try:
        return VersionInfo.from_message(await client.receive_json())
    finally:
        await client.close()