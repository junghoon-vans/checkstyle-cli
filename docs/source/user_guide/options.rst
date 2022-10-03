===============
List of options
===============

Index
=====

- :option:`checkstyle --help`
- :option:`checkstyle --config`
- :option:`checkstyle --version`
- :option:`checkstyle --runtime-version`
- :option:`checkstyle --debug`


Description
===========

.. program:: checkstyle
.. option:: -h, --help

    Show a description that how to use checkstyle.

    Command-line example:

    .. code-block::

        $ checkstyle -h
        $ checkstyle --help

.. option:: -c, --config

    Set configuration file of checkstyle.

    * default: ``google``
    * The configuration is specified using the path or keyword(``sun`` and ``google``).

    Command-line example:

    .. code-block::

        $ checkstyle -c sun
        $ checkstyle --config path/to/config/file

.. option:: -V, --version

    Show program's version number and exit.

    Command-line example:

    .. code-block::

        $ checkstyle -V
        $ checkstyle --version

.. option:: --runtime-version

    Set ``runtime version`` of checkstyle.

    * default: |DefaultRuntime|

    Command-line example:

    .. parsed-literal::

        $ checkstyle --runtime-version |DefaultRuntime|


.. option:: -d, --debug

    Print debug logging of checkstyle.

    Command-line example:

    .. code-block::

        $ checkstyle -d
        $ checkstyle --debug
