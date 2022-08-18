import os

import requests
from appdirs import user_cache_dir
from tqdm import tqdm


class Store:

    def download_checkstyle(self, version: str) -> str:
        filename = self._get_checkstyle_filename(version)
        if not self._is_exist_file(filename):
            try:
                self._download(
                    url=self._get_checkstyle_download_url(version),
                    filename=self._get_checkstyle_filename(version),
                    target=self.get_checkstyle_cache(filename),
                )
            except requests.exceptions.HTTPError as e:
                print(e)
        return filename

    def get_checkstyle_cache(self, filename: str) -> str:
        cache_path = user_cache_dir('checkstyle')
        if not os.path.exists(cache_path):
            os.makedirs(cache_path)
        return os.path.join(cache_path, filename)

    def _get_checkstyle_filename(self, version: str) -> str:
        _prefix_filename = "checkstyle-{version}-all.jar"

        if version == 'latest':
            version = self._get_latest_checkstyle_version()

        filename = _prefix_filename.format(version=version)
        return filename

    def _get_latest_checkstyle_version(self) -> str:
        response = requests.get(
            "https://api.github.com/repos/checkstyle/checkstyle"
            "/releases/latest",
        )
        latest_tag = response.json()['tag_name']
        latest_version = latest_tag.strip('checkstyle-')
        return latest_version

    def _is_exist_file(self, filename: str) -> bool:
        return os.path.exists(self.get_checkstyle_cache(filename))

    def _get_checkstyle_download_url(self, version: str) -> str:
        _prefix_url = "https://github.com/checkstyle/checkstyle/" \
            "releases/download/checkstyle-{version}/"
        download_url = _prefix_url.format(version=version)
        return download_url

    def _download(self, url: str, filename: str, target: str) -> None:
        r = requests.get(url + filename, stream=True)
        r.raise_for_status()
        total = int(r.headers.get('Content-Length', 0))

        with open(target, "wb") as f, tqdm(
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
