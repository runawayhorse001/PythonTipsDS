.. _primer:

================
Primer Functions 
================

.. |py| replace:: ``Python``
.. |pyc| replace:: ``:: Python Code:``
.. |out| replace:: ``:: Ouput:``
.. |eg| replace:: ``:: Example:``

.. note::

	This Chapter :ref:`primer` is for beginner.  If you have some |py| programming experience, you may skip this chapter. 


The following ``functions`` have been heavily used in my daily Data Scientist work.


``*``
+++++

Single asterisk as used in function declaration allows variable number of arguments passed from calling environment. Inside the function it behaves as a tuple.

|pyc|

	.. code-block:: python

		my_list = [1,2,3]
		print(my_list)
		print(*my_list)

|out|

	.. code-block:: python

		[1, 2, 3]
		1 2 3


``range``
+++++++++


|pyc|

	.. code-block:: python

		print(range(5))
		print(*range(5))
		print(*range(3,8))

|out|

	.. code-block:: python

		range(0, 5)
		0 1 2 3 4
		3 4 5 6 7



``random``
++++++++++	

More details can be found at: 

a. ``random``: https://docs.python.org/3/library/random.html#random.randint

b. ``np.random``: https://docs.scipy.org/doc/numpy/reference/routines.random.html

``random.random``
------------------

|pyc|

	.. code-block:: python

		import random
		random.random()

		# (b - a) * random() + a
		random.uniform(3,8)


|out|

	.. code-block:: python

		0.33844051243073625
		7.772024014335885

``np.random``
-------------

|pyc|

	.. code-block:: python

		np.random.random_sample()
		np.random.random_sample(4)
		np.random.random_sample([2,4])

		# (b - a) * random_sample() + a
		a = 3; b = 8
		(b-a)*np.random.random_sample([2,4])+a


|out|

	.. code-block:: python

		0.11919402208670005
		array([0.07384755, 0.9005251 , 0.30030561, 0.38221819])
		array([[0.76851156, 0.56973309, 0.47074505, 0.7814957 ],
		       [0.5778028 , 0.94653057, 0.51193493, 0.48693931]])

		array([[4.65799262, 6.32702018, 6.55545234, 5.45877784],
		       [7.69941994, 4.68709357, 5.49790728, 4.60913966]])

``round``
+++++++++

Sometimes, we really do not need the scientific decimals for ``output`` results. So you can use this function to round an array to the given number of decimals.

|pyc|

	.. code-block:: python

		np.round(np.random.random_sample([2,4]),2)

|out|

	.. code-block:: python

		array([[0.76, 0.06, 0.41, 0.4 ],
		       [0.07, 0.51, 0.84, 0.76]])


TODO..
++++++

|pyc|

.. code-block:: python


|out|

.. code-block:: python






|pyc|

.. code-block:: python


|out|

.. code-block:: python





|pyc|

.. code-block:: python


|out|

.. code-block:: python




|pyc|

.. code-block:: python


|out|

.. code-block:: python

