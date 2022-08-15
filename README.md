checkstyle-cli
===

[![PyPI version](https://img.shields.io/pypi/v/checkstyle-cli?style=flat-square)](https://pypi.org/project/checkstyle-cli/)
![python versions](https://img.shields.io/pypi/pyversions/checkstyle-cli?style=flat-square)

A command-line tool for checkstyle.

Requirements
---

- Java >= 8

Installation
---

### Using cli

```bash
> pip install checkstyle-cli
```

### Using pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
repos:
  - repo: https://github.com/junghoon-vans/checkstyle-hooks
    rev: v0.3.0 # Use the ref you want
    hooks:
    - id: checkstyle
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
  - default: `google`
    - `sun` and `google` are embedded options.
- `-v`, `--version`
  - version to run checkstyle
  - default: `latest`

License
---

[MIT License](https://github.com/junghoon-vans/checkstyle-cli/blob/main/LICENSE)