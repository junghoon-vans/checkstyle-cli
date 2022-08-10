checkstyle-cli
===

checkstyle-cli is a tool that easily installs and executes checkstyle.

Usage
---

```bash
pip install checkstyle-cli
checkstyle -c /sun_checks.xml -v 10.3.2 .
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