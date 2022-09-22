"""Utils package"""
import os.path
import subprocess
from typing import List


def run_command(
        binary_file: str,
        base_dir: str,
        args: List[str],
        files: List[str],
) -> int:
    """Function for running java program

        Args:
            binary_file: Binary file to run the program
            base_dir: Directory where the binary file is located
            args: Arguments passed to the program
            files: Target files passed to the program

        Returns:
            int: Exit code

    """
    cmd = ['java', '-jar', os.path.join(base_dir, binary_file)] + args + files

    result = subprocess.run(
        args=cmd,
        capture_output=True,
        encoding="UTF-8",
    )

    exit_code = result.returncode
    output = result.stdout or result.stderr
    print(output)

    if result.check_returncode is not None:
        print(f"Process finished with exit code {exit_code}")

    return exit_code
