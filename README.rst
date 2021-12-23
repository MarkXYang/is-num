is-num
======
.. image:: https://img.shields.io/pypi/v/is-num   
    :target: https://pypi.org/project/is-num/
    :alt: PyPI

A Python library to determine if something is a number.

Installation
------------

.. code-block:: bash

    pip install is-num

Developing
----------

This project uses ``black`` to format code and ``flake8`` for linting. We also support ``pre-commit`` to ensure these have been run. To configure your local environment please install these development dependencies and set up the commit hooks.

.. code-block:: bash

    $ pip install black flake8 pre-commit
    $ pre-commit intall
Testing
-------

This project uses ``pytest`` to run tests and also to test docstring examples.

Install the test dependencies.

.. code-block:: bash

    $ pip install -r requirements_test.txt

Run the tests.
.. code-block:: bash

    $ pytest
    === 3 passed in 0.13 seconds ===
