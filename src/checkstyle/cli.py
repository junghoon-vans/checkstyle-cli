"""Command-line implementation of checkstyle-cli"""
from typing import Optional
from typing import Sequence

from checkstyle import application


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Main function to run application

        Args:
            argv: Arguments vector

        Returns:
            int: Exit code

    """
    app = application.Application()
    exit_code = app.run(argv)
    return exit_code
