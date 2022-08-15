from typing import Optional
from typing import Sequence

from checkstyle import application


def main(argv: Optional[Sequence[str]] = None) -> int:
    app = application.Application()
    exit_code = app.run(argv)
    return exit_code
