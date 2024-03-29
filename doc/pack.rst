
.. _pack:

===============
Package Wrapper
===============

It's super easy to wrap your own package in Python. I packed some functions which I frequently 
used in my daily work. You can download and install it from `My statspy library`_. The hierarchical 
structure and the directory structure of this package are as follows. 
 
Hierarchical Structure
++++++++++++++++++++++


.. code-block:: bash

	├── README.md
	├── __init__.py
	├── requirements.txt
	├── setup.py
	├── statspy
	│   ├── __init__.py
	│   ├── basics.py
	│   └── tests.py
	└── test
	    ├── nb
	    │   └── t.test.ipynb
	    └── test1.py

	3 directories, 9 files


From the above hierarchical structure, you will find that you have to have ``__init__.py`` in each directory. I will explain the ``__init__.py`` file with the example below:

Set Up
++++++

.. code-block:: python

	from setuptools import setup, find_packages

	try:
	    with open("README.md") as f:
	        long_description = f.read()
	except IOError:
	    long_description = ""

	try:
	    with open("requirements.txt") as f:
	        requirements = [x.strip() for x in f.read().splitlines() if x.strip()]
	except IOError:
	    requirements = []

	setup(name='statspy',
	      install_requires=requirements,
	      version='1.0',
	      description='Statistics python library',
	      author='Wenqiang Feng',
	      author_email='von198@gmail.com',
	      license="MIT",
	      url='git@github.com:runawayhorse001/statspy.git',
	      packages=find_packages(),
	      long_description=long_description,
	      long_description_content_type="text/markdown",
	      classifiers=[
	        "License :: OSI Approved :: MIT License",
	        "Programming Language :: Python",
	        "Programming Language :: Python :: 2",
	        "Programming Language :: Python :: 3",
	      ],
	      include_package_data=True	      
	     )


.. note::

    If you want to compile the ``conda`` package, you can add the following
    code in your ``setup.py``:

    1. import ``import distutils.command.bdist_conda``:

    .. code-block:: python

       import distutils.command.bdist_conda

    2. pass the options to setup():

    .. code-block:: python

        distclass=distutils.command.bdist_conda.CondaDistribution)

        # eg
        setup(
        name="conda_example",
        version="1.0",
        distclass=distutils.command.bdist_conda.CondaDistribution,
        conda_buildnum=1,)

    Then, you can use the following code in terminal to compile the conda
    package:

    .. code-block:: python

        python setup.py bdist_conda

Requirements
++++++++++++

.. code-block:: rst

	pandas
	numpy
	scipy
	patsy
	matplotlib



ReadMe
++++++

.. code-block:: bash

	# StatsPy

	This is my statistics python library repositories.
	The ``API`` can be found at: https://runawayhorse001.github.io/statspy. 
	If you want to colne and install it, you can use 

	- clone

	```{bash}
	git clone git@github.com:runawayhorse001/statspy.git
	```
	- install 

	```{bash}
	cd statspy
	pip install -r requirements.txt 
	python setup.py install
	```
	- uninstall 

	```{bash}
	pip uninstall statspy
	```

	- test 

	```{bash}
	cd statspy/test
	python test1.py
	```







.. _My ststspy library: https://runawayhorse001.github.io/statspy/
