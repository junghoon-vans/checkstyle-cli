import os

import requests
from tqdm import tqdm


class Store:
    def download_checkstyle(self, version: str) -> str:
        filename = self._get_checkstyle_filename(version)
        if not self._is_exist_file(filename):
            try:
                url = self._get_checkstyle_download_url(version)
                self._download(url=url, filename=filename)
            except requests.exceptions.HTTPError as e:
                print(e)
        return filename

    def get_checkstyle_cache(self, filename: str) -> str:
        cache_path = os.path.join(os.getcwd(), ".checkstyle_cache")
        if not os.path.exists(cache_path):
            os.makedirs(cache_path)
        return os.path.join(cache_path, filename)

    def _get_checkstyle_filename(self, version: str) -> str:
        _prefix_filename = "checkstyle-{version}-all.jar"
        filename = _prefix_filename.format(version=version)
        return filename

    def _is_exist_file(self, filename: str) -> bool:
        return os.path.exists(self.get_checkstyle_cache(filename))

    def _get_checkstyle_download_url(self, version: str) -> str:
        _prefix_url = "https://github.com/checkstyle/checkstyle/" \
            "releases/download/checkstyle-{version}/"
        download_url = _prefix_url.format(version=version)
        return download_url

    def _download(self, url: str, filename: str) -> None:
        r = requests.get(url + filename, stream=True)
        r.raise_for_status()
        total = int(r.headers.get('Content-Length', 0))

        with open(self.get_checkstyle_cache(filename), "wb") as f, tqdm(
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
