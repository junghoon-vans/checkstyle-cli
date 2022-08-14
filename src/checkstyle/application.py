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

        target = utils.download_checkstyle(kwargs.pop('version'))
        args = [
            '-c', kwargs.pop('config'),
        ]
        files = kwargs.pop('files')

        exit_code = utils.run_command(target, (args+files))
        return exit_code

    def parse_kargs(self, argv: Optional[Sequence[str]]) -> Dict[str, Any]:
        args, unknown = self._parser.parse_known_args(argv)
        kwargs = vars(args)
        return kwargs
