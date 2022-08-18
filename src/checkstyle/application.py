from typing import Optional
from typing import Sequence

from checkstyle.utils import run_command
from checkstyle.utils.parser import Parser
from checkstyle.utils.store import Store


class Application:
    def __init__(self) -> None:
        self._parser = Parser()
        self._store = Store()

    def run(self, argv: Optional[Sequence[str]]) -> int:
        args_dict = self._parser.parse_args_dict(argv)

        version = args_dict.pop('version')
        files = args_dict.pop('files')

        filename = self._store.download_checkstyle(version)

        exit_code = run_command(
            target=self._store.get_checkstyle_cache(filename=filename),
            args=self._parser.convert_args_dict_to_list(args_dict) + files,
        )
        return exit_code
