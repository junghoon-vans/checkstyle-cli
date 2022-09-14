from argparse import ArgumentParser
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Sequence

from checkstyle import __version__
from checkstyle import default_runtime


def convert_args_dict_to_list(kwargs) -> List[str]:
    result = []
    for k, v in kwargs.items():
        result.append("-"+k[0])
        result.append(v)
    return result


def _is_google_or_sun(config: str) -> bool:
    return config == 'google' or config == 'sun'


class Parser:
    _parser = ArgumentParser()

    def __init__(self) -> None:
        self._parser.add_argument(
            "-c",
            "--config",
            type=str,
            default="google",
            help="checkstyle configuration file",
        )
        self._parser.add_argument(
            "-V",
            "--version",
            action='version',
            version=f'checkstyle-cli {__version__}',
        )
        self._parser.add_argument(
            "--runtime-version",
            type=str,
            default=default_runtime,
            help="checkstyle version",
        )
        self._parser.add_argument(
            "files", nargs="*",
            help="files to verify",
        )

    def parse_args_dict(self, argv: Optional[Sequence[str]]) -> Dict[str, Any]:
        args, unknown = self._parser.parse_known_args(argv)
        args_dict = vars(args)

        if _is_google_or_sun(args_dict['config']):
            args_dict['config'] = "/{name}_checks.xml".format(
                name=args_dict['config'],
            )

        return args_dict
