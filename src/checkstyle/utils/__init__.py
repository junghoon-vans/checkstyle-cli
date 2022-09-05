import os.path
import subprocess
from typing import List


def run_command(filename: str, cache_dir: str, args: List[str]) -> int:
    cmd = ['java', '-jar', os.path.join(cache_dir, filename)] + args

    result = subprocess.run(
        args=cmd,
        capture_output=True,
        encoding="UTF-8",
    )

    exit_code = result.returncode
    output = result.stdout or result.stderr
    print(output)

    if result.check_returncode is not None:
        print(
            "Process finished with exit code {exit_code}".format(
                exit_code=exit_code,
            ),
        )

    return exit_code
