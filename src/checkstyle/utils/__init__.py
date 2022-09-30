"""Utils package"""
import os.path
import subprocess
from typing import Any
from typing import Dict
from typing import List


def run_command(
        binary_file: str,
        base_dir: str,
        files: List[str],
        **kwargs,
) -> int:
    """Function for running java program

        Args:
            binary_file: Binary file to run the program
            base_dir: Directory where the binary file is located
            files: Target files passed to the program
            kwargs: Keyword arguments passed to the program

        Returns:
            int: Exit code

    """
    cmd = ['java', '-jar', os.path.join(base_dir, binary_file)]

    result = subprocess.run(
        cmd + get_command_args_from(kwargs) + files,
        capture_output=True,
        encoding="UTF-8",
    )

    print(result.stderr)
    print(result.stdout)

    exit_code = result.returncode

    if result.check_returncode is not None:
        print(f"Process finished with exit code {exit_code}")

    return exit_code


def get_command_args_from(kwargs: Dict[str, Any]) -> List[str]:
    """Returns arguments list for running command
        Args:
            kwargs: Keyword arguments

        Returns:
            list(str): Arguments list
    """
    args = []

    for k, v in kwargs.items():
        if type(v) is not bool:
            args.append(k)
            args.append(v)
        elif v is True:
            args.append(k)

    return args
