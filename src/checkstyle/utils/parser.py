from argparse import ArgumentParser
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Sequence


class Parser:
    _parser = ArgumentParser()

    def __init__(self) -> None:
        self._parser.add_argument(
            "-c",
            "--config",
            type=str,
            default="/google_checks.xml",
            help="checkstyle configuration file",
        )
        self._parser.add_argument(
            "-v",
            "--version",
            type=str,
            default="10.3.2",
            help="checkstyle version",
        )
        self._parser.add_argument(
            "files", nargs="*",
            help="files to verify",
        )

    def parse_args_dict(self, argv: Optional[Sequence[str]]) -> Dict[str, Any]:
        args, unknown = self._parser.parse_known_args(argv)
        return vars(args)

    def convert_args_dict_to_list(self, kwargs) -> List[str]:
        result = []
        for k, v in kwargs.items():
            result.append("-"+k[0])
            result.append(v)
        return result
