"""Module for handling checkstyle binaries"""
import os

import requests
from appdirs import user_cache_dir
from tqdm import tqdm


def download_checkstyle(fetch_dir: str, version: str = 'latest') -> str:
    """Download checkstyle binary file

        Args:
            fetch_dir: Download location
            version: Checkstyle runtime version

        Returns:
            Binary filename

    """
    if version == 'latest':
        version = _get_latest_checkstyle_version()

    filename = get_checkstyle_filename(version)
    if not is_exist_file(filename, fetch_dir):
        try:
            _download(
                url=_get_checkstyle_download_url(version),
                filename=get_checkstyle_filename(version),
                fetch_dir=fetch_dir,
            )
        except requests.exceptions.HTTPError as e:
            print(e)
    return filename


def is_exist_file(filename: str, fetch_dir: str) -> bool:
    """Checking for existence of binary file

        Args:
            filename: Checkstyle binary filename
            fetch_dir: Download location

        Returns:
            If binary file already exists, return True

    """
    return os.path.exists(os.path.join(fetch_dir, filename))


def get_checkstyle_filename(version: str) -> str:
    """Return binary filename from version

        Args:
            version: Checkstyle runtime version

        Returns:
            Checkstyle binary filename

    """
    filename = f"checkstyle-{version}-all.jar"
    return filename


def get_checkstyle_cache_dir() -> str:
    """Return checkstyle cache directory

        Returns:
            Cache directory

    """
    cache_dir = user_cache_dir('checkstyle')
    os.makedirs(cache_dir, exist_ok=True)
    return cache_dir


def _get_checkstyle_download_url(version: str) -> str:
    """Return checkstyle binary download URL from version

        Args:
            version: Checkstyle runtime version

        Returns:
            Checkstyle binary download URL

    """
    download_url = "https://github.com/checkstyle/checkstyle/" \
        f"releases/download/checkstyle-{version}/"
    return download_url


def _get_latest_checkstyle_version() -> str:
    """Convert arguments dictionary to list

        Returns:
            Latest checkstyle version

    """
    response = requests.get(
        "https://api.github.com/repos/checkstyle/checkstyle"
        "/releases/latest",
    )
    latest_tag = response.json()['tag_name']
    latest_version = latest_tag.strip('checkstyle-')
    return latest_version


def _download(url: str, filename: str, fetch_dir: str) -> None:
    """Execute downloading

        Args:
            url: Download URL
            filename: Download filename
            fetch_dir: Fetch directory

        Returns:
            Arguments list

    """
    r = requests.get(url + filename, stream=True)
    r.raise_for_status()
    total = int(r.headers.get('Content-Length', 0))

    with open(os.path.join(fetch_dir, filename), "wb") as f, tqdm(
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
