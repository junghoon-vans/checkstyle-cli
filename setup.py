import os
import sys

from distutils.command.build import build as orig_build
from distutils.core import Command
from setuptools import setup
from setuptools.command.install import install as orig_install


if __name__ == "__main__":   # import checkstyle module
    sys.path.insert(
        0, os.path.join(
            os.path.dirname(
                os.path.abspath(__file__),
            ), 'src',
        ),
    )
    from checkstyle import default_runtime
    from checkstyle.utils.store import download_checkstyle
    from checkstyle.utils.store import get_checkstyle_cache_dir


class build(orig_build):
    sub_commands = orig_build.sub_commands + [('fetch_binaries', None)]


class install(orig_install):
    sub_commands = orig_install.sub_commands + [('install_checkstyle', None)]


class fetch_binaries(Command):
    build_lib = None

    def initialize_options(self):
        pass

    def finalize_options(self):
        self.set_undefined_options('build', ('build_lib', 'build_lib'))

    def run(self):
        fetch_dir = os.path.join(
            self.build_lib, 'checkstyle/.checkstyle_cache',
        )

        if not os.path.exists(fetch_dir):
            os.makedirs(fetch_dir)

        download_checkstyle(
            version=default_runtime,
            fetch_dir=fetch_dir,
        )


class install_checkstyle(Command):
    build_lib = None

    def initialize_options(self):
        pass

    def finalize_options(self):
        self.set_undefined_options('build', ('build_lib', 'build_lib'))

    def run(self):
        self.copy_tree(
            infile=os.path.join(
                self.build_lib, 'checkstyle/.checkstyle_cache',
            ),
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
