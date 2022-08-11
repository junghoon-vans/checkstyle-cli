from typing import Optional
from typing import Sequence

from checkstyle.main import application


def main(argv: Optional[Sequence[str]] = None):
    app = application.Application()
    app.run(argv)
