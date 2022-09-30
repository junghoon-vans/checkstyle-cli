## v0.6.0 (2022-09-30)

### Feat

- Add debug options to print debug logs

### Fix

- Update test_parser to resolve assertion error

### Refactor

- Change args to kwargs for command execution
- Update run_command function to add files param

## v0.5.0 (2022-09-20)

### Fix

- Resolve no module named error while deploying readthedocs
- Resolve '_static' does not exist error

### Refactor

- Rename param in run_command function

## v0.4.0 (2022-09-14)

### Feat

- Change fetch dir to build_temp
- Fetch binary on file on build time
- Print errout if it exist
- Add version option to check program version
- Rename option for setting runtime version to checkstyle_version
- Add default_runtime variable

### Fix

- Resolve fail to download binary of latest version

### Refactor

- Update setup.py to override install class
- Change option for setting runtime to --runtime-version
- Rename path params to fetch_dir or cache_dir
- Add path param to file check method
- Change target param to filename and path
- Change methods to static method

## v0.3.2 (2022-08-18)

### Fix

- Resolve comparative operator error

## v0.3.1 (2022-08-18)

### Feat

- Change default option of config to google
- Add config options to parser
- Change default option of version to latest
- Add latest option to parser

### Refactor

- Change checkstyle cache path

## v0.3.0 (2022-08-15)

### Feat

- Add utils package
- Add convert args dict to list function
- Add exit_code as return value

### Fix

- Fix typo

### Refactor

- Add store to utils package
- Add parser to utils package
- Add target param to run_command
- Change way to parse argv

## v0.2.4 (2022-08-14)

### Fix

- Resolve no module error

### Refactor

- Add __init__.py to tests package

## v0.2.3 (2022-08-14)

### Feat

- Add tests package for testing

### Refactor

- Rename main package to checkstyle

## v0.2.2 (2022-08-10)

## v0.2.1 (2022-08-10)

## v0.2.0 (2022-08-10)

### Feat

- Create checkstyle cache path
- Add download progress bar
- Add is_exist_file function
- Update run_checkstyle function
- Add download_checkstyle function
- Add version argv to arg_parser

### Refactor

- Rename parse_options to parse_args

## v0.1.0-beta (2022-08-09)

### Feat

- Create main package
- Create application class
- Add pre_commit_hooks package

### Refactor

- Rename filenames arg to files
