checkstyle-cli
===

[![PyPI version](https://img.shields.io/pypi/v/checkstyle-cli?style=flat-square)](https://pypi.org/project/checkstyle-cli/)
![python versions](https://img.shields.io/pypi/pyversions/checkstyle-cli?style=flat-square)

A command-line tool for checkstyle.

Installation
---

```bash
> pip install checkstyle-cli
```

Usage
---

```bash
> checkstyle -h
usage: checkstyle [-h] [-c CONFIG] [-v VERSION]
                  [files ...]

> checkstyle -c /sun_checks.xml -v 10.3.2 .
```

### Positional Arguments

- `files`
  - files to verify 

### Optional Arguments

- `-c`, `--config`
  - configuration XML file path
  - default: `/google_checks.xml`
    - `/sun_checks.xml` and `/google_checks.xml` are embedded options.
- `-v`, `--version`
  - version to run checkstyle
  - default: `10.3.2`

License
---

[MIT Licencse](https://github.com/junghoon-vans/checkstyle-cli/blob/main/LICENSE)