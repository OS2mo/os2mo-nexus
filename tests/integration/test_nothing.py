# SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
import pytest


@pytest.mark.integration_test
async def test_nothing_1() -> None:
    assert True


@pytest.mark.integration_test
async def test_nothing_2() -> None:
    assert True
