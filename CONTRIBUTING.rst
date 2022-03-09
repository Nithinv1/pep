Contributing Guidelines
=======================

To learn more about the purpose of PEPs and how to go about writing one, please
start reading at `PEP 1 <https://www.python.org/dev/peps/pep-0001/>`_.
Also, make sure to check the `README <./README.rst>`_ for information
on how to render the PEPs in this repository.
Thanks again for your contributions, and we look forward to reviewing them!


Before writing a new PEP
------------------------

Prior to submitting a pull request here with your draft PEP, see `PEP 1
<https://www.python.org/dev/peps/pep-0001/#start-with-an-idea-for-python>`_
for some important steps to consider, including proposing and discussing it
first in an appropriate venue, drafting a PEP and gathering feedback, and
developing at least a prototype reference implementation of your idea.


Commit messages and PR titles
-----------------------------

When adding or modifying a PEP, please always include the PEP number in the
commit summary and pull request title.
For example, ``PEP NNN: <summary of changes>``.


Sign the CLA
------------

Before you hit "Create pull request", please take a moment to ensure that this
project can legally accept your contribution by verifying you have signed the
`PSF Contributor Agreement <https://www.python.org/psf/contrib/contrib-form/>`_.

If you haven't signed the CLA before, please follow the
`steps outlined in the CPython devguide
<https://devguide.python.org/pullrequest/#licensing>`_ to do so.


Code of Conduct
---------------

All interactions for this project are covered by the
`PSF Code of Conduct <https://www.python.org/psf/codeofconduct/>`_. Everyone is
expected to be open, considerate, and respectful of others, no matter their
position within the project.


Run pre-commit linting locally
------------------------------

You can run this repo's basic linting suite locally,
either on-demand, or automatically against modified files
whenever you commit your changes.

They are also run in CI, so you don't have to run them locally, though doing
so will help you catch and potentially fix common mistakes before pushing
your changes and opening a pull request.

This repository uses the `pre-commit <https://pre-commit.com/>`_ tool to
install, configure and update a suite of hooks that check for
common problems and issues, and fix many of them automatically.

If your system has ``make`` installed, you can run the pre-commit checkers
on the full repo by running ``make lint``. This will
install pre-commit in the current virtual environment if it isn't already,
so make sure you've activated the environment you want it to use
before running this command.

Otherwise, you can install pre-commit with

.. code-block:: bash

    python -m pip install pre-commit

(or your choice of installer), and then run the hooks on all the files
in the repo with

.. code-block:: bash

    pre-commit run --all-files

or only on any files that have been modified but not yet committed with

.. code-block:: bash

    pre-commit run

If you would like pre-commit to run automatically against any modified files
every time you commit, install the hooks with

.. code-block:: bash

    pre-commit install

Then, whenever you ``git commit``, pre-commit will run and report any issues
it finds or changes it makes, and abort the commit to allow you to check,
and if necessary correct them before committing again.


Check and fix PEP spelling
--------------------------

To check for common spelling mistakes in your PEP and automatically suggest
corrections, you can run the codespell tool through pre-commit as well.

Like the linters, on a system with ``make`` available, it can be installed
(in the currently-activated environment) and run on all files in the
repository with a single command, ``make spellcheck``.

For finer control or on other systems, after installing pre-commit as in
the previous section, you can run it against only the files
you've modified and not yet committed with

.. code-block:: bash

    pre-commit run --hook-stage manual codespell

or against all files with

.. code-block:: bash

    pre-commit run --all-files --hook-stage manual codespell

**Note**: While fixing spelling mistakes as part of more substantive
copyediting and proofreading of draft and active PEPs is okay,
we generally advise against PRs that simply mass-correct minor typos on
older PEPs that don't significantly impair meaning and understanding,
as these tend to create a fairly high level of noise and churn for
PEP readers, authors and editors relative to the amount of practical value
they provide.
