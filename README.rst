checkstyle-cli
==============

|PyPI version| |pre-commit.ci status| |GitHub Workflow Status| |Documentation Status|

A command-line tool for |Checkstyle|_.

Requirements
------------

   See |Requirements Documentation Page|_.

The minimum ``JRE`` version required depends on runtime of checkstyle.

Getting Started
---------------

   See |Quickstart Documentation Page|_.

cli
~~~

.. code:: bash

   $ pip install checkstyle-cli

pre-commit
~~~~~~~~~~

Add this to your ``.pre-commit-config.yaml``

.. parsed-literal::

   repos:
     - repo: https://github.com/junghoon-vans/checkstyle-cli
       rev: |release|
       hooks:
       - id: checkstyle

License
-------

`MIT
License <https://github.com/junghoon-vans/checkstyle-cli/blob/main/LICENSE>`__

.. |Checkstyle| replace:: checkstyle
.. _Checkstyle: https://checkstyle.sourceforge.io
.. |Requirements Documentation Page| replace:: requirements documentation
.. _Requirements Documentation Page: https://checkstyle-cli.readthedocs.io/en/latest/user_guide/requirements.html
.. |Quickstart Documentation Page| replace:: quickstart documentation
.. _Quickstart Documentation Page: https://checkstyle-cli.readthedocs.io/en/latest/index.html#quickstart

.. |PyPI version| image:: https://img.shields.io/pypi/v/checkstyle-cli
   :target: https://pypi.org/project/checkstyle-cli/
.. |pre-commit.ci status| image:: https://results.pre-commit.ci/badge/github/junghoon-vans/checkstyle-cli/main.svg
   :target: https://results.pre-commit.ci/latest/github/junghoon-vans/checkstyle-cli/main
.. |GitHub Workflow Status| image:: https://img.shields.io/github/actions/workflow/status/junghoon-vans/checkstyle-cli/python-publish.yml?branch=v0.7.0
.. |Documentation Status| image:: https://readthedocs.org/projects/checkstyle-cli/badge/?version=latest
   :target: https://checkstyle-cli.readthedocs.io/en/latest/?badge=latest

.. |release| replace:: v0.7.0
