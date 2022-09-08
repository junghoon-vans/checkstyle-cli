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


class build(orig_build):
    sub_commands = orig_build.sub_commands + [('fetch_binaries', None)]


class install(orig_install):
    sub_commands = orig_install.sub_commands + [('install_checkstyle', None)]


class fetch_binaries(Command):
    build_temp = None

    def initialize_options(self):
        pass

    def finalize_options(self):
        self.set_undefined_options('build', ('build_temp', 'build_temp'))

    def run(self):
        if not os.path.exists(self.build_temp):
            os.makedirs(self.build_temp)

        download_checkstyle(
            version=default_runtime,
            fetch_dir=self.build_temp,
        )


class install_checkstyle(Command):
    build_temp = None

    def initialize_options(self):
        pass

    def finalize_options(self):
        self.set_undefined_options('build', ('build_temp', 'build_temp'))

    def run(self):
        self.copy_tree(
            infile=self.build_temp,
            outfile=get_checkstyle_cache_dir(),
        )


setup(
    cmdclass={
        'build': build,
        'fetch_binaries': fetch_binaries,
        'install': install,
        'install_checkstyle': install_checkstyle,
    },
)
