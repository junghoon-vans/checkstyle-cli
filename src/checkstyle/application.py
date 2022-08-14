import subprocess
from argparse import Namespace
from typing import List
from typing import Optional
from typing import Sequence
from typing import Tuple

from checkstyle import utils


class Application:
    def __init__(self) -> None:
        self._parser = utils.arg_parser()

    def run(self, argv: Optional[Sequence[str]]):
        args, unknown = self.parse_args(argv)
        self.run_checkstyle(args)

    def run_checkstyle(self, args: Namespace):
        version = args.version
        filename = utils.download_checkstyle(version)

        cmd = [
            'java', '-jar', utils.get_checkstyle_cache(filename),
            '-c', args.config,
        ]
        files = args.files
        subprocess.run(cmd + files)

    def parse_args(
        self, argv: Optional[Sequence[str]],
    ) -> Tuple[Namespace, List[str]]:
        return self._parser.parse_known_args(argv)
