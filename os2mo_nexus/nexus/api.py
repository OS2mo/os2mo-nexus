# SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from authlib.integrations.httpx_client import AsyncOAuth2Client

from os2mo_nexus.config import NexusSettings


class NexusAPI:
    def __init__(self, settings: NexusSettings) -> None:
        self.settings = settings

    @asynccontextmanager
    async def open(self) -> AsyncGenerator[None]:
        self.client = AsyncOAuth2Client(
            base_url=self.settings.url,
            client_id=self.settings.oidc.client_id,
            client_secret=self.settings.oidc.client_secret,
            grant_type="client_credentials",
            token_endpoint=self.settings.oidc.token_endpoint,
            # TODO (https://github.com/lepture/authlib/issues/531): Hack to enable
            # automatic fetching of token on first call, instead of only refreshing.
            token={"expires_at": -1, "access_token": ""},
        )
        async with self.client:
            yield

    async def entrypoint(self) -> dict:
        r = (await self.client.get("/api/core/mobile/unity/v2/")).json()
        return r

    async def todo(self) -> None:
        r = await self.client.get("/api/core/mobile/unity/v2/")
        r = r.json()
        x = r["_links"]["stsCdiCases"]["href"]
        r = await self.client.get(x)
        print("rrr", r)
