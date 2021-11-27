
.. _pypi:

=======================
Publish Package to PyPI
=======================

In this chapter, you’ll learn how to upload your own package to PyPI. 
 
Register PyPI account
+++++++++++++++++++++

If you do not have a PyPI accout, you need to register an account at https://pypi.org/account/register .


Install ``twine``
+++++++++++++++++

.. code-block:: bash

	pip install twine

Build Your Package
+++++++++++++++++++++

.. code-block:: python

	python setup.py sdist bdist_wheel

Then you will get a new folder ``dist``:

.. code-block:: bash

	.
	├── PyAudit-1.0-py3-none-any.whl
	├── PyAudit-1.0-py3.6.egg
	└── PyAudit-1.0.tar.gz


Upload Your Package
+++++++++++++++++++

.. code-block:: bash

	twine upload dist/*

During the uploading processing, you need to provide your PyPI account ``username`` and ``password``:

.. code-block:: bash

	Enter your username: runawayhorse001
	Enter your password:

Package at PyPI
+++++++++++++++

Here is my ``PyAudit`` package at [PyPI](https://pypi.org/project/PyAudit). You can install ``PyAudit`` using:

.. code-block:: bash

    pip install PyAudit



.. _My ststspy library: https://runawayhorse001.github.io/statspy/
