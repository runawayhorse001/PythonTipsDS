.. _struct:

===============
Data Structures
===============

.. |nb| replace:: ``Jupyter Notebook``
.. |py| replace:: ``Python``
.. |pyc| replace:: ``:: Python Code:``
.. |out| replace:: ``:: Output:``
.. |eg| replace:: ``:: Example:``
.. |syn| replace:: ``::syntax:``


.. note::

	This Chapter :ref:`struct` is for beginner.  If you have some |py| programming experience, you may skip this chapter. 

``List``, ``Set``, ``Tuple``, and ``Dictionary`` are most common and basic data structures in Python.
This chapter will cover some basic python commands with these data structure.

These data structures are different in their Mutability and Order, shown in the image below:

    .. figure:: images/data_structures.png

- You can use curly braces to define a set like this: {1, 2, 3}. However,
  if you leave the curly braces empty like this: {}, Python will instead
  create an empty dictionary. So to create an empty set, use set().
- A dictionary itself is mutable, but each of its individual keys must be
  immutable. You can find out why here.

Reference:
Data Structures- Lists, Tuples, Dictionaries, and Sets in Python:
https://medium.com/@aitarurachel/data-structures-with-lists-tuples-dictionaries-and-sets-in-python-612245a712af


List
++++

``list`` is one of data structures which is heavily using in my daily work.

Create empty list
-----------------

The empty list is used to initialize a list.

|pyc|

    .. code-block:: python

        # list can be defined with square brackets.
        my_list = []
        # create empty list with list() constructor
        # when no parameters are passed
        my_list = list()
        type(my_list)

|out|

	.. code-block:: python

		list

I applied the empty list to initialize my ``silhouette score`` list when I try to find the 
optimal number of the clusters. 

|eg|

	.. code-block:: python

		min_cluster = 3
		max_cluster =8

		# silhouette_score
		scores = []

		for i in range(min_cluster, max_cluster):
		    score = np.round(np.random.random_sample(),2)
		    scores.append(score)

		print(scores)

|out|

	.. code-block:: python

		[0.16, 0.2, 0.3, 0.87, 0.59]



Unpack list
-----------

|eg|

	.. code-block:: python

		num = [1,2,3,4,5,6,7,8,9,10]
		print(*num)

|out|

	.. code-block:: python

		1 2 3 4 5 6 7 8 9 10


Methods of list objects
-----------------------

Methods of list objects:

+-----------------------------+-------------------------------------+
| Name                        |                      Description    |
+=============================+=====================================+
| list. ``append(x)``         | Add an item to the end of the list  |
+-----------------------------+-------------------------------------+
| list. ``extend(iterable)``  | Extend the list by appending all    |
+-----------------------------+-------------------------------------+
| list. ``insert(i, x)``      | Insert an item at a given position  |
+-----------------------------+-------------------------------------+
| list. ``remove(x)``         | Remove the first item               |
+-----------------------------+-------------------------------------+
| list. ``pop([i])``          | Remove the item at given position   |
+-----------------------------+-------------------------------------+
| list. ``clear()``           | Remove all items from the list      |
+-----------------------------+-------------------------------------+
| list. ``index(x[,s[,e]])``  | Return zero-based index in the list |
+-----------------------------+-------------------------------------+
| list. ``count(x)``          | Return the number of times x        |
+-----------------------------+-------------------------------------+
| list. ``sort(key,reverse)`` | Sort the items of the list          |
+-----------------------------+-------------------------------------+
| list. ``reverse()``         | Reverse the elements of the list    |
+-----------------------------+-------------------------------------+
| list. ``copy()``            | Return a shallow copy [#f1]_ of list|
+-----------------------------+-------------------------------------+

list.append(x) vs. list.extend(iterable)
----------------------------------------

The difference of list. ``append(x)`` vs. list. ``extend(iterable)`` is easy to understand
from the example below:

|eg|

    .. code-block:: python

        list1 = ['A','B','C']
        list2 = ['D','E','F']
        list1.append(list2)
        print(list1)

|out|

	.. code-block:: python

		['A', 'B', 'C', ['D', 'E', 'F']]

|eg|

    .. code-block:: python

        list1 = ['A','B','C']
        list2 = ['D','E','F']
        list1.extend(list2)
        print(list1)


|out|

	.. code-block:: python

		['A', 'B', 'C', 'D', 'E', 'F']


.. rubric:: Footnotes

.. [#f1] Shallow Copy vs Deep Copy Reference: https://stackoverflow.com/posts/184780/revisions

   Shallow copy:

   	.. figure:: images/shal.png 
    
   The variables A and B refer to different areas of memory, when B is assigned to A the two variables refer to the same area of memory. Later modifications to the contents of either are instantly reflected in the contents of other, as they share contents.

   Deep Copy:    

   	.. figure:: images/deep.png 

   The variables A and B refer to different areas of memory, when B is assigned to A the values in the memory area which A points to are copied into the memory area to which B points. Later modifications to the contents of either remain unique to A or B; the contents are not shared. 




Tuple
+++++

A tuple is an assortment of data, separated by commas, which makes it similar to the Python list, but a tuple is fundamentally different in that a tuple is "immutable." This means that it cannot be changed, modified, or manipulated.


Create Tuple
------------

A tuple is defined in the same way as a list, except that all elements are enclosed in parentheses instead of square brackets.
To create a tuple of one item, it's required a trailing comma after the item.
Without the comma, Python just assumes you have an extra pair of parentheses instead of creating a tuple.

|pyc|

    .. code-block:: python

        # initialize an empty tuple by using the tuple function
        my_tuple = tuple()

        # tuple with one value must include trailing comma
        my_tuple = ('A', )
        type(my_tuple)

        # string type if no trailing comma
        my_str = ('A')
        type(my_str)

        # convert list to tuple
        my_list = ['A','B','C']
        my_tuple = tuple(my_list)
        type(my_tuple)

|out|

	.. code-block:: python

		tuple
		str
		tuple

Assigning Multiple Values At Once with Tuple
--------------------------------------------
A cool way of using tuple is to assign multiple values at once.

|eg|

    .. code-block:: python

        (x, y, z) = ('A','B','C')
        (MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)


Dictionary
++++++++++

``dict`` is one of another data structures which is heavily using in my daily work. I heavily applied the ``dict`` in my ``PyAudit`` package, more details can be found at `PyAudit`_.

Create ``dict`` from lists
--------------------------

|eg|

	.. code-block:: python

		col_names = ['name','Age', 'Sex', 'Car']
		col_values = ['Michael', '30', 'Male', ['Honda','Tesla']]
		# 
		d = {key: value for key, value in zip(col_names, col_values)}
		print(d)
		#
		import pandas as pd

		df = pd.DataFrame(d)
		print(df)

|out|

	.. code-block:: python

		{'name': 'Michael', 'Age': '30', 'Sex': 'Male', 'Car': ['Honda', 'Tesla']}
		      name Age   Sex    Car
		0  Michael  30  Male  Honda
		1  Michael  30  Male  Tesla

``dict.get()``
--------------

When ``get()`` is called, Python checks if the specified key exists in the dict. If it does, then ``get()`` returns the value of that key. If the key does not exist, then ``get()`` returns the value specified in the second argument to ``get()``. A good application of ``get()`` can be found at :ref:`update_keys_dict`.

|eg|

	.. code-block:: python

		data1 = d.get("name", "best")
		data2 = d.get("names", "George")
		print(data1)  # Michael
		print(data2)  # George

|out|

	.. code-block:: python

		Michael
		George


Looping Techniques
------------------

|eg|

	.. code-block:: python

		print([(key, val) for key, val in d.items()])

|out|

	.. code-block:: python

		[('name', 'Michael'), ('Age', '30'), ('Sex', 'Male'), ('Car', ['Honda', 'Tesla'])]


Update Values in Dict
---------------------

1. Replace values in dict

	|eg|

		.. code-block:: python

			replace = {'Car': ['Tesla S', 'Tesla X']}
			print(d)
			d.update(replace)
			print(d)

	|out|

		.. code-block:: python

			{'name': 'Michael', 'Age': '30', 'Sex': 'Male', 'Car': ['Honda', 'Tesla']}
			{'name': 'Michael', 'Age': '30', 'Sex': 'Male', 'Car': ['Tesla S', 'Tesla X']}

2. Add key and values in dict

	|eg|

		.. code-block:: python

			# add key and values in dict
			added = {'Kid': ['Tom', 'Jim']}
			print(d)
			d.update(added)
			print(d)

	|out|

		.. code-block:: python

			{'name': 'Michael', 'Age': '30', 'Sex': 'Male', 'Car': ['Tesla S', 'Tesla X']}
			{'name': 'Michael', 'Age': '30', 'Sex': 'Male', 'Car': ['Tesla S', 'Tesla X'], 'Kid': ['Tom', 'Jim']}

.. _update_keys_dict:

Update Keys in Dict
-------------------

|eg|

	.. code-block:: python

		# update keys in dict
		mapping = {'Car': 'Cars', 'Kid': 'Kids'}
		#
		print({mapping.get(key, key): val for key, val in d.items()})

|out|

	.. code-block:: python

		{'name': 'Michael', 'Age': '30', 'Sex': 'Male', 'Car': ['Tesla S', 'Tesla X'], 'Kid': ['Tom', 'Jim']}
		{'name': 'Michael', 'Age': '30', 'Sex': 'Male', 'Cars': ['Tesla S', 'Tesla X'], 'Kids': ['Tom', 'Jim']}


One line if-else statement
++++++++++++++++++++++++++

With filter
-----------

|syn|

	.. code-block:: python

		[ RESULT for x in seq if COND ]


|pyc|

	.. code-block:: python

		num = [1,2,3,4,5,6,7,8,9,10]

		[x for x in num if x%2 ==0]

|out|

	.. code-block:: python

		[2, 4, 6, 8, 10]


Without filter
--------------

|syn|

	.. code-block:: python

		[ RESULT1 if COND1  else RESULT2 if COND2 else RESULT3 for x in seq]


|pyc|

	.. code-block:: python

		num = [1,2,3,4,5,6,7,8,9,10]

		['Low' if 1<= x <=3 else 'Median' if 3<x<8 else 'High' for x in num]

|out|

	.. code-block:: python

		['Low',
		 'Low',
		 'Low',
		 'Median',
		 'Median',
		 'Median',
		 'Median',
		 'High',
		 'High',
		 'High']	

[VanderPlas2016]_ [McKinney2013]_ 


.. _PyAudit: https://github.com/runawayhorse001/PyAudit/blob/master/PyAudit/basics.py#L251-L340