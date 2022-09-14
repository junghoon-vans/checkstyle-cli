from typing import Optional
from typing import Sequence

from checkstyle.utils import run_command
from checkstyle.utils.parser import convert_args_dict_to_list
from checkstyle.utils.parser import Parser
from checkstyle.utils.store import download_checkstyle
from checkstyle.utils.store import get_checkstyle_cache_dir


class Application:
    def __init__(self) -> None:
        self._parser = Parser()

    def run(self, argv: Optional[Sequence[str]]) -> int:
        args_dict = self._parser.parse_args_dict(argv)

        version = args_dict.pop('runtime_version')
        files = args_dict.pop('files')

        filename = download_checkstyle(
            version=version, fetch_dir=get_checkstyle_cache_dir(),
        )

        exit_code = run_command(
            filename=filename,
            cache_dir=get_checkstyle_cache_dir(),
            args=convert_args_dict_to_list(args_dict) + files,
        )
        return exit_code
