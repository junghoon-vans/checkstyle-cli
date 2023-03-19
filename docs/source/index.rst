==============
checkstyle-cli
==============

A command-line tool for checkstyle.

Quickstart
==========

Installation
------------

To install **checkstyle-cli**, run this command.

.. code::

   $ pip install checkstyle-cli

If you want **checkstyle-cli** to be used for **pre-commit**, Add this to your ``.pre-commit-config.yaml``.

.. parsed-literal::

   repos:
  - repo: https://github.com/junghoon-vans/checkstyle-cli
    rev: |release| # Use the ref you want
    hooks:
    - id: checkstyle

Usage
-----

.. code::

   $ checkstyle [options] [files...]

   # run on current path with default options
   $ checkstyle .

   # run with custom options
   $ checkstyle -c custom_config.xml --runtime-version 10.9.2 path/to/project


User Guide
==========

.. toctree::
   :maxdepth: 2

   user_guide/index

API documentation
=================

.. toctree::
   :maxdepth: 2

   api/index

Changelog
=========

.. toctree::
   :maxdepth: 2

   changelog


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
