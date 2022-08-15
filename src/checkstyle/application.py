from typing import Optional
from typing import Sequence

from checkstyle.utils import download_checkstyle
from checkstyle.utils import get_checkstyle_cache
from checkstyle.utils import run_command
from checkstyle.utils.parser import Parser


class Application:
    def __init__(self) -> None:
        self._parser = Parser()

    def run(self, argv: Optional[Sequence[str]]) -> int:
        args_dict = self._parser.parse_args_dict(argv)

        binary_file = download_checkstyle(args_dict.pop('version'))
        files = args_dict.pop('files')

        exit_code = run_command(
            target=get_checkstyle_cache(binary_file),
            args=self._parser.convert_args_dict_to_list(args_dict) + files,
        )
        return exit_code
