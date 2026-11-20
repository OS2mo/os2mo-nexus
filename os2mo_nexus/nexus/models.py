# SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from pydantic import BaseModel as PydanticBaseModel
from pydantic import Extra
from pydantic import Field


class NexusBase(PydanticBaseModel):
    class Config:
        allow_population_by_field_name = True

        # The flow of e.g. importing a user from FK-org is as follows:
        #
        # 1. Fetch a prototype object from 'importProfessionalFromSts'.
        # 2. Modify the values as needed.
        # 3. POST the modified prototype - including all unmodified properties
        #    - as the body of the 'create' link in the prototype's _links.
        #
        # Because prototypes contain properties we don't modify as part of this
        # integration, and because they must be sent back unchanged apart from
        # our modifications, we allow and retain extra fields:
        extra = Extra.allow


class Link(NexusBase):
    href: str


class Home(NexusBase):
    class Links(NexusBase):
        importProfessionalFromSts: Link

    links: Links = Field(alias="_links")
