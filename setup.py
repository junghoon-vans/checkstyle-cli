import os
import sys

from distutils.command.build import build as orig_build
from distutils.core import Command
from setuptools import setup
from setuptools.command.install import install as orig_install

SOURCE_DIR = os.path.join(os.path.dirname(__file__), 'src')

if __name__ == "__main__":   # import checkstyle module
    sys.path.insert(0, SOURCE_DIR)
    from checkstyle import default_runtime
    from checkstyle.utils.store import download_checkstyle
    from checkstyle.utils.store import get_checkstyle_cache_dir


class Build(orig_build):
    sub_commands = orig_build.sub_commands + [('fetch_binaries', None)]


class FetchBinaries(Command):
    build_dir = None

    def initialize_options(self):
        pass

    def finalize_options(self):
        self.set_undefined_options('build', ('build_temp', 'build_dir'))

    def run(self):
        if not os.path.exists(self.build_dir):
            os.makedirs(self.build_dir)

        download_checkstyle(
            version=default_runtime,
            fetch_dir=self.build_dir,
        )


class Install(orig_install):
    build_dir = None

    def initialize_options(self):
        super().initialize_options()

    def finalize_options(self):
        self.set_undefined_options('build', ('build_temp', 'build_dir'))
        super().finalize_options()

    def run(self):
        self.copy_tree(self.build_dir, get_checkstyle_cache_dir())
        super().run()


setup(
    cmdclass={
        'build': Build,
        'fetch_binaries': FetchBinaries,
        'install': Install,
    },
)
