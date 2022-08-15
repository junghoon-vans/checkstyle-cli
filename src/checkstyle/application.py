from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Sequence

from checkstyle import utils


class Application:
    def __init__(self) -> None:
        self._parser = utils.arg_parser()

    def run(self, argv: Optional[Sequence[str]]) -> int:
        args_dict = self.parse_args_dict(argv)

        binary_file = utils.download_checkstyle(args_dict.pop('version'))
        files = args_dict.pop('files')

        exit_code = utils.run_command(
            target=utils.get_checkstyle_cache(binary_file),
            args=self.convert_args_dict_to_list(args_dict) + files,
        )
        return exit_code

    def parse_args_dict(self, argv: Optional[Sequence[str]]) -> Dict[str, Any]:
        args, unknown = self._parser.parse_known_args(argv)
        return vars(args)

    def convert_args_dict_to_list(self, kwargs) -> List[str]:
        result = []
        for k, v in kwargs.items():
            result.append("-"+k[0])
            result.append(v)
        return result
