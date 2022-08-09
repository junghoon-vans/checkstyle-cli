import argparse
import os

import requests
from tqdm import tqdm


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


def download_checkstyle(version: str) -> str:
    filename = get_checkstyle_filename(version)
    if not is_exist_file(filename):
        try:
            url = get_checkstyle_download_url(version)
            download(url=url, filename=filename)
        except requests.exceptions.HTTPError as e:
            print(e)
    return filename


def is_exist_file(filename: str) -> bool:
    return os.path.exists(get_checkstyle_cache(filename))


def get_checkstyle_download_url(version: str) -> str:
    _prefix_url = "https://github.com/checkstyle/checkstyle/" \
        "releases/download/checkstyle-{version}/"
    download_url = _prefix_url.format(version=version)
    return download_url


def get_checkstyle_filename(version: str) -> str:
    _prefix_filename = "checkstyle-{version}-all.jar"
    filename = _prefix_filename.format(version=version)
    return filename


def get_checkstyle_cache(filename: str) -> str:
    cache_path = os.path.join(os.getcwd(), ".checkstyle_cache")
    if not os.path.exists(cache_path):
        os.makedirs(cache_path)
    return os.path.join(cache_path, filename)


def download(url: str, filename: str) -> None:
    r = requests.get(url + filename, stream=True)
    r.raise_for_status()
    total = int(r.headers.get('Content-Length', 0))

    with open(get_checkstyle_cache(filename), "wb") as f, tqdm(
        desc=filename,
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        f.write(r.content)
        for data in r.iter_content(chunk_size=1024):
            size = f.write(data)
            bar.update(size)
