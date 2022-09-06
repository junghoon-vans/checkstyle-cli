checkstyle-cli
===

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/junghoon-vans/checkstyle-cli/develop.svg)](https://results.pre-commit.ci/latest/github/junghoon-vans/checkstyle-cli/main)
[![PyPI version](https://img.shields.io/pypi/v/checkstyle-cli?style=flat-square)](https://pypi.org/project/checkstyle-cli/)
![python versions](https://img.shields.io/pypi/pyversions/checkstyle-cli?style=flat-square)

A command-line tool for checkstyle.

Requirements
---

The minimum `JRE` version required depends on runtime of checkstyle.

| checkstyle version | JRE version |
| ------------------ | ----------- |
| 10.x               | >= 11       |
| 7.x, 8.x 9.x       | >= 8        |
| 6.x                | >= 6        |
| 5.x                | >= 5        |

Installation
---

### cli

```bash
> pip install checkstyle-cli
```

### pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
repos:
  - repo: https://github.com/junghoon-vans/checkstyle-cli
    rev: v0.4.0 # Use the ref you want
    hooks:
    - id: checkstyle
```

Usage
---

```bash
> checkstyle [options] [files...]

# run on current path with default options
> checkstyle .

# run with custom options
> checkstyle -c custom_config.xml --runtime-version 10.3.2 ~/workspace/demo
```

Options
---

### `-c`, `--config`

- configuration XML file path
- default: `google`
  - `sun` and `google` are embedded options.

### `-v`, `--version`

- show program's version number and exit

### `--runtime-version`

- set runtime version of checkstyle
- default: `10.3.3`

Caching
---

When you run a `checkstyle` command, it automatically fetches the required files and saves them in the following path:

- Linux: `~/.cache/checkstyle`
- Mac OS X: `~/Library/Caches/checkstyle`
- Windows: `%LocalAppData%\checkstyle\checkstyle\Cache`

License
---

[MIT License](https://github.com/junghoon-vans/checkstyle-cli/blob/main/LICENSE)