import subprocess
from argparse import Namespace
from typing import List
from typing import Optional
from typing import Sequence
from typing import Tuple

from main import utils


class Application:
    def __init__(self) -> None:
        self._parser = utils.arg_parser()

    def run(self, argv: Optional[Sequence[str]]):
        args, unknown = self.parse_options(argv)
        self.run_checkstyle(args)

    def run_checkstyle(self, args: Namespace):
        cmd = [
            'java', '-jar', 'checkstyle-10.3.2-all.jar',
            '-c', args.config,
        ]
        filenames = args.filenames
        subprocess.run(cmd + filenames)

    def parse_options(
        self, argv: Optional[Sequence[str]],
    ) -> Tuple[Namespace, List[str]]:
        return self._parser.parse_known_args(argv)
