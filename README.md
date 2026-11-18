<!--
SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
SPDX-License-Identifier: MPL-2.0
-->

# OS2mo: KMD Nexus

## Testing

Testing requires a running [OS2mo](https://github.com/os2mo/os2mo) stack and a
connection to the KMD Nexus test environment (Unity). Note that Unity may be
unstable or unavailable on Thursdays, when KMD resets the data. Create a
`nexus.env`:

```env
# https://vault.bitwarden.com/#/vault?itemId=eb8d4019-ed87-45c6-a7e2-b50600c92d72
NEXUS__OIDC__CLIENT_SECRET=hunter2
```

Tests can now be run using [pytest](https://pytest.org), for example:

```sh
podman compose run --rm nexus pytest tests/integration/test_something.py::test_foo
```
