import pytest
from checkstyle.application import Application


@pytest.fixture
def application() -> Application:
    application = Application()
    return application


def test_parse_args(application: Application):
    assert application.parse_kwargs(None) == {
        'config': '/google_checks.xml', 'version': '10.3.2', 'files': [],
    }
