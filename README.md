checkstyle-cli
===

[![PyPI version](https://img.shields.io/pypi/v/checkstyle-cli)](https://pypi.org/project/checkstyle-cli/)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/junghoon-vans/checkstyle-cli/develop.svg)](https://results.pre-commit.ci/latest/github/junghoon-vans/checkstyle-cli/develop)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/junghoon-vans/checkstyle-cli/Upload%20Python%20Package)
[![Documentation Status](https://readthedocs.org/projects/checkstyle-cli/badge/?version=latest)](https://checkstyle-cli.readthedocs.io/en/latest/?badge=latest)

A command-line tool for checkstyle.

Requirements
---

> See [requirements documentation](https://checkstyle-cli.readthedocs.io/en/latest/user_guide/requirements.html).

The minimum `JRE` version required depends on runtime of checkstyle.

Getting Started
---

> See [quickstart documentation](https://checkstyle-cli.readthedocs.io/en/latest/index.html#quickstart).

### cli

```bash
$ pip install checkstyle-cli
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

License
---

[MIT License](https://github.com/junghoon-vans/checkstyle-cli/blob/main/LICENSE)