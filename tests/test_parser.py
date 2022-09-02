import pytest
from checkstyle.utils.parser import Parser

from src.checkstyle import default_runtime


@pytest.fixture
def parser() -> Parser:
    parser = Parser()
    return parser


def test_parse_args(parser: Parser):
    assert parser.parse_args_dict(None) == {
        'config': '/google_checks.xml',
        'version': default_runtime, 'files': [],
    }
