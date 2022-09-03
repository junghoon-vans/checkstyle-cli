import os

import requests
from appdirs import user_cache_dir
from tqdm import tqdm


def download_checkstyle(version: str, path: str) -> str:
    if version == 'latest':
        version = _get_latest_checkstyle_version()

    filename = _get_checkstyle_filename(version)
    if not _is_exist_file(filename, path):
        try:
            _download(
                url=_get_checkstyle_download_url(version),
                filename=_get_checkstyle_filename(version),
                path=path,
            )
        except requests.exceptions.HTTPError as e:
            print(e)
    return filename


def get_checkstyle_cache_path() -> str:
    cache_path = user_cache_dir('checkstyle')
    if not os.path.exists(cache_path):
        os.makedirs(cache_path)
    return cache_path


def _get_checkstyle_download_url(version: str) -> str:
    _prefix_url = "https://github.com/checkstyle/checkstyle/" \
        "releases/download/checkstyle-{version}/"
    download_url = _prefix_url.format(version=version)
    return download_url


def _get_latest_checkstyle_version() -> str:
    response = requests.get(
        "https://api.github.com/repos/checkstyle/checkstyle"
        "/releases/latest",
    )
    latest_tag = response.json()['tag_name']
    latest_version = latest_tag.strip('checkstyle-')
    return latest_version


def _download(url: str, filename: str, path: str) -> None:
    r = requests.get(url + filename, stream=True)
    r.raise_for_status()
    total = int(r.headers.get('Content-Length', 0))

    with open(os.path.join(path, filename), "wb") as f, tqdm(
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


def _get_checkstyle_filename(version: str) -> str:
    _prefix_filename = "checkstyle-{version}-all.jar"
    filename = _prefix_filename.format(version=version)
    return filename


def _is_exist_file(filename: str, path: str) -> bool:
    return os.path.exists(os.path.join(path, filename))
