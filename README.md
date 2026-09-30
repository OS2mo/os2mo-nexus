<!--
SPDX-FileCopyrightText: Magenta ApS <https://magenta.dk>
SPDX-License-Identifier: MPL-2.0
-->

# OS2mo: KMD Nexus

## Testing

Testing requires a running [OS2mo](https://github.com/os2mo/os2mo) stack. Tests
can be run using [pytest](https://pytest.org), for example:

```sh
podman compose run --rm nexus pytest tests/integration/test_something.py::test_foo
```
