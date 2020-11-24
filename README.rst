========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-cscli/badge/?style=flat
    :target: https://readthedocs.org/projects/python-cscli
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/ryohare/python-cscli.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ryohare/python-cscli

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/ryohare/python-cscli?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/ryohare/python-cscli

.. |requires| image:: https://requires.io/github/ryohare/python-cscli/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/ryohare/python-cscli/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/ryohare/python-cscli/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/ryohare/python-cscli

.. |commits-since| image:: https://img.shields.io/github/commits-since/ryohare/python-cscli/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/ryohare/python-cscli/compare/v0.0.0...master



.. end-badges

Command line tool for interacting with Crowdstrike Falcon.

* Free software: MIT license

Installation
============

::

    pip install cscli

You can also install the in-development version with::

    pip install https://github.com/ryohare/python-cscli/archive/master.zip


Documentation
=============


https://python-cscli.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
