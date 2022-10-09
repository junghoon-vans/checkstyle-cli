checkstyle-cli
==============

|PyPI version| |pre-commit.ci status| |GitHub Workflow Status| |Documentation Status|

A command-line tool for checkstyle.

Requirements
------------

   See `requirements
   documentation <https://checkstyle-cli.readthedocs.io/en/latest/user_guide/requirements.html>`__.

The minimum ``JRE`` version required depends on runtime of checkstyle.

Getting Started
---------------

   See `quickstart
   documentation <https://checkstyle-cli.readthedocs.io/en/latest/index.html#quickstart>`__.

cli
~~~

.. code:: bash

   $ pip install checkstyle-cli

pre-commit
~~~~~~~~~~

Add this to your ``.pre-commit-config.yaml``

.. code:: yaml

   repos:
     - repo: https://github.com/junghoon-vans/checkstyle-cli
       rev: v0.4.0 # Use the ref you want
       hooks:
       - id: checkstyle

License
-------

`MIT
License <https://github.com/junghoon-vans/checkstyle-cli/blob/main/LICENSE>`__

.. |PyPI version| image:: https://img.shields.io/pypi/v/checkstyle-cli
   :target: https://pypi.org/project/checkstyle-cli/
.. |pre-commit.ci status| image:: https://results.pre-commit.ci/badge/github/junghoon-vans/checkstyle-cli/develop.svg
   :target: https://results.pre-commit.ci/latest/github/junghoon-vans/checkstyle-cli/develop
.. |GitHub Workflow Status| image:: https://img.shields.io/github/workflow/status/junghoon-vans/checkstyle-cli/Upload%20Python%20Package
.. |Documentation Status| image:: https://readthedocs.org/projects/checkstyle-cli/badge/?version=latest
   :target: https://checkstyle-cli.readthedocs.io/en/latest/?badge=latest
