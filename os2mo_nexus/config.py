# SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0

from fastramqpi.config import Settings as FastRAMQPISettings
from pydantic import AnyHttpUrl
from pydantic import BaseModel
from pydantic import BaseSettings


class NexusOIDCSettings(BaseModel):
    client_id: str
    client_secret: str
    token_endpoint: AnyHttpUrl
    scope: str


class NexusSettings(BaseModel):
    url: AnyHttpUrl
    oidc: NexusOIDCSettings


class Settings(BaseSettings):
    class Config(BaseSettings.Config):
        frozen = True
        env_nested_delimiter = "__"

    fastramqpi: FastRAMQPISettings
    nexus: NexusSettings | None
