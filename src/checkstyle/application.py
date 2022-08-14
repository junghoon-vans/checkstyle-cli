from typing import Any
from typing import Dict
from typing import Optional
from typing import Sequence

from checkstyle import utils


class Application:
    def __init__(self) -> None:
        self._parser = utils.arg_parser()

    def run(self, argv: Optional[Sequence[str]]) -> int:
        kwargs = self.parse_kargs(argv)
        exit_code = self.run_checkstyle(kwargs)
        return exit_code

    def run_checkstyle(self, kwargs: dict) -> int:
        filename = utils.download_checkstyle(kwargs.pop('version'))
        files = kwargs.pop('files')
        cmd = [
            'java', '-jar', utils.get_checkstyle_cache(filename),
            '-c', kwargs.pop('config'),
        ]
        exit_code = utils.run_command(*(cmd + files))
        return exit_code

    def parse_kargs(self, argv: Optional[Sequence[str]]) -> Dict[str, Any]:
        args, unknown = self._parser.parse_known_args(argv)
        kwargs = vars(args)
        return kwargs
