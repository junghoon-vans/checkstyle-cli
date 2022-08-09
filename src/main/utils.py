import argparse
import os

import requests


def arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--config",
        type=str,
        default="/google_checks.xml",
        help="checkstyle configuration file",
    )
    parser.add_argument(
        "-v",
        "--version",
        type=str,
        default="10.3.2",
        help="checkstyle version",
    )
    parser.add_argument(
        "files", nargs="*",
        help="files to verify",
    )
    return parser


def download_checkstyle(version: str) -> None:
    try:
        download(
            url=get_checkstyle_download_url(version),
            filename=get_checkstyle_filename(version),
        )
    except requests.exceptions.HTTPError as e:
        print(e)


def get_checkstyle_download_url(version: str) -> str:
    _prefix_url = "https://github.com/checkstyle/checkstyle/" \
        "releases/download/checkstyle-{version}/"
    download_url = _prefix_url.format(version=version)
    return download_url


def get_checkstyle_filename(version: str) -> str:
    _prefix_filename = "checkstyle-{version}-all.jar"
    filename = _prefix_filename.format(version=version)
    return filename


def download(url: str, filename: str) -> None:
    r = requests.get(url + filename)
    r.raise_for_status()

    with open(os.path.join(os.getcwd(), filename), "wb") as f:
        f.write(r.content)
