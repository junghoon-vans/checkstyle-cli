import subprocess
from typing import List


def run_command(target: str, args: List[str]) -> int:
    cmd = ['java', '-jar', target] + args

    result = subprocess.run(
        args=cmd,
        capture_output=True,
        encoding="UTF-8",
    )

    output = result.stdout
    exit_code = result.returncode

    print(output)
    if result.check_returncode is not None:
        print(
            "Process finished with exit code {exit_code}".format(
                exit_code=exit_code,
            ),
        )

    return exit_code
