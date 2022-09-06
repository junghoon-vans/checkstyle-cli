import pytest
from checkstyle import default_runtime
from checkstyle.utils.parser import Parser


@pytest.fixture
def parser() -> Parser:
    parser = Parser()
    return parser


def test_parse_args(parser: Parser):
    assert parser.parse_args_dict(None) == {
        'config': '/google_checks.xml', 'files': [],
        'runtime_version': default_runtime,
    }
