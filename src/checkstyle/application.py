from argparse import Namespace
from typing import List
from typing import Optional
from typing import Sequence
from typing import Tuple

from checkstyle import utils


class Application:
    def __init__(self) -> None:
        self._parser = utils.arg_parser()

    def run(self, argv: Optional[Sequence[str]]) -> int:
        args, unknown = self.parse_args(argv)
        exit_code = self.run_checkstyle(args)
        return exit_code

    def run_checkstyle(self, args: Namespace) -> int:
        version = args.version
        filename = utils.download_checkstyle(version)

        cmd = [
            'java', '-jar', utils.get_checkstyle_cache(filename),
            '-c', args.config,
        ]
        files = args.files
        exit_code = utils.run_command(*(cmd + files))
        return exit_code

    def parse_args(
        self, argv: Optional[Sequence[str]],
    ) -> Tuple[Namespace, List[str]]:
        return self._parser.parse_known_args(argv)
