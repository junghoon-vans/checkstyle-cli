"""Module containing the application class"""
from typing import Optional
from typing import Sequence

from checkstyle.utils import run_command
from checkstyle.utils.parser import Parser
from checkstyle.utils.store import download_checkstyle
from checkstyle.utils.store import get_checkstyle_cache_dir


class Application:
    """Application class"""

    def __init__(self) -> None:
        self._parser = Parser()

    def run(self, argv: Optional[Sequence[str]]) -> int:
        """Run application

            Args:
                argv: Arguments vector

            Returns:
                int: Exit code

        """
        args_dict = self._parser.parse_args_dict(argv)

        binary_file = download_checkstyle(
            version=args_dict.pop('runtime_version'),
            fetch_dir=get_checkstyle_cache_dir(),
        )

        exit_code = run_command(
            binary_file=binary_file,
            base_dir=get_checkstyle_cache_dir(),
            files=args_dict.pop('files'),
            **args_dict,
        )
        return exit_code
