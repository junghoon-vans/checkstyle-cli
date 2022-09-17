"""Utils package"""
import os.path
import subprocess
from typing import List


def run_command(filename: str, base_dir: str, args: List[str]) -> int:
    """Function for running java program

        Args:
            filename: Binary file to run
            base_dir: Directory where the binary file is located
            args: Arguments needed to run the program

        Returns:
            int: Exit code

    """
    cmd = ['java', '-jar', os.path.join(base_dir, filename)] + args

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
