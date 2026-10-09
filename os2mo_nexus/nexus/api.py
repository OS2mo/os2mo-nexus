# SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from authlib.integrations.httpx_client import AsyncOAuth2Client

from os2mo_nexus.config import NexusSettings


class NexusAPI:
    def __init__(self, settings: NexusSettings) -> None:
        self.settings = settings
        self.client = AsyncOAuth2Client(
            base_url=settings.url,
            client_id=settings.oidc.client_id,
            client_secret=settings.oidc.client_secret,
            grant_type="client_credentials",
            token_endpoint=settings.oidc.token_endpoint,
            # TODO (https://github.com/lepture/authlib/issues/531): Hack to enable
            # automatic fetching of token on first call, instead of only refreshing.
            token={"expires_at": -1, "access_token": ""},
        )

    @asynccontextmanager
    async def open(self) -> AsyncGenerator[None]:
        async with self.client:
            yield
