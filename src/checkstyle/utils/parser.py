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
            default="google",
            help="checkstyle configuration file",
        )
        self._parser.add_argument(
            "-v",
            "--version",
            type=str,
            default="latest",
            help="checkstyle version",
        )
        self._parser.add_argument(
            "files", nargs="*",
            help="files to verify",
        )

    def parse_args_dict(self, argv: Optional[Sequence[str]]) -> Dict[str, Any]:
        args, unknown = self._parser.parse_known_args(argv)
        args_dict = vars(args)

        if self._is_google_or_sun(args_dict['config']):
            args_dict['config'] = "/{name}_checks.xml".format(
                name=args_dict['config'],
            )

        return args_dict

    def convert_args_dict_to_list(self, kwargs) -> List[str]:
        result = []
        for k, v in kwargs.items():
            result.append("-"+k[0])
            result.append(v)
        return result

    def _is_google_or_sun(self, config: str):
        return config == 'google' or 'sun'
