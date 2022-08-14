from argparse import Namespace

import pytest
from checkstyle.application import Application


@pytest.fixture
def application() -> Application:
    application = Application()
    return application


def test_parse_args(application: Application):
    assert application.parse_args(None) == (
        Namespace(config='/google_checks.xml', version='10.3.2', files=[]), [],
    )
