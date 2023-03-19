import pytest
from checkstyle.utils.parser import Parser


@pytest.fixture
def parser() -> Parser:
    parser = Parser()
    return parser


def test_parse_args(parser: Parser):
    assert parser.parse_args_dict(None) == {
        'files': [],
        'runtime_version': 'latest',
        '-c': '/google_checks.xml',
        '-d': False,
        '-o': None,
        '-f': 'plain',
    }
