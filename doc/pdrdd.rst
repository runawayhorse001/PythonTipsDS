.. _pdrdd:


=========================================
``pd.DataFrame`` vs ``PySpark DataFrame``
=========================================



.. |nb| replace:: ``Jupyter Notebook``
.. |zp| replace:: ``Zeppelin``
.. |py| replace:: ``Python``
.. |pyc| replace:: ``:: Python Code:``
.. |out| replace:: ``:: Output:``
.. |eg| replace:: ``:: Example:``
.. |comp| replace:: ``:: Comparison:``


.. .. note::

..	This Chapter :ref:`nb` is for beginner.  If you have some |py| programming experience, you may skip this chapter.


Create DataFrame
++++++++++++++++

From List
---------

.. code-block:: python

	my_list = [['a', 1, 2], ['b', 2, 3],['c', 3, 4]]
	col_name = ['A', 'B', 'C']

|pyc|

.. code-block:: python

	# caution for the columns=
	pd.DataFrame(my_list,columns= col_name)
	#
	spark.createDataFrame(my_list, col_name).show()


|comp|

.. code-block:: python

	                  +---+---+---+
	                  |  A|  B|  C|
	   A  B  C        +---+---+---+
	0  a  1  2        |  a|  1|  2|
 	1  b  2  3        |  b|  2|  3|
 	2  c  3  4        |  c|  3|  4|
 	                  +---+---+---+

.. attention::

   Pay attention to the parameter ``columns=`` in ``pd.DataFrame``. Since the default value will make the list as rows.


	|pyc|

	.. code-block:: python

		# caution for the columns=
		pd.DataFrame(my_list, columns= col_name)
		#
		pd.DataFrame(my_list, col_name)


	|comp|

	.. code-block:: python

		   A  B  C             0  1  2	 	
		0  a  1  2          A  a  1  2
		1  b  2  3          B  b  2  3
		2  c  3  4          C  c  3  4

From Dict
---------

.. code-block:: python

	d = {'A': [0, 1, 0],
	     'B': [1, 0, 1],
	     'C': [1, 0, 0]}

|pyc|

.. code-block:: python

	pd.DataFrame(d)for 
	# Tedious for PySpark
 	spark.createDataFrame(np.array(list(d.values())).T.tolist(),list(d.keys())).show()

|comp|

.. code-block:: python

	                   +---+---+---+
	                   |  A|  B|  C|
	   A  B  C         +---+---+---+
	0  0  1  1         |  0|  1|  1|
	1  1  0  0         |  1|  0|  0|
	2  0  1  0         |  0|  1|  0|
	                   +---+---+---+

Convert between pandas and pyspark DataFrame
++++++++++++++++++++++++++++++++++++++++++++

From pandas to pyspark DataFrame
--------------------------------
|eg|

.. code-block:: python

    # pd.DataFrame pandas_df: DataFrame pandas
    # rdd.DataFrame. spark_df: DataFrame spark
    pandas_df = pd.read_csv('Advertising.csv')
    spark_df = spark.createDataFrame(pandas_df)
    spark_df.printSchema()

From pyspark to pandas DataFrame
--------------------------------
|eg|

.. code-block:: python

    pandas_df = spark_df.toPandas()
    pandas_df.info()

Load DataFrame
++++++++++++++

From DataBase
-------------

Most of time, you need to share your code with your colleagues or release your code for Code Review or Quality assurance(QA). You will definitely do not want to have your ``User Information`` in the code. So you can save them
in login.txt:

.. code-block:: rst

	runawayhorse001
	PythonTips

and use the following code to import your ``User Information``:

.. code-block:: python

	#User Information
	try: 
	    login = pd.read_csv(r'login.txt', header=None)
	    user = login[0][0]
	    pw = login[0][1]
	    print('User information is ready!')
	except:
	    print('Login information is not available!!!')

	#Database information
	host = '##.###.###.##'
	db_name = 'db_name' 
	table_name = 'table_name'

|comp|

.. code-block:: python

	conn = psycopg2.connect(host=host, database=db_name, user=user, password=pw)
	cur = conn.cursor()

	sql = """
	      select *
	      from {table_name}
	      """.format(table_name=table_name)
	pandas_df = pd.read_sql(sql, conn)

.. code-block:: python

	# connect to database
	url = 'jdbc:postgresql://'+host+':5432/'+db_name+'?user='+user+'&password='+pw
	properties ={'driver': 'org.postgresql.Driver', 'password': pw,'user': user}
	spark_df = spark.read.jdbc(url=url, table=table_name, properties=properties)


.. attention::

	Reading tables from Database with PySpark neespark_df the proper drive for the corresponding Database. For example, the above demo neespark_df org.postgresql.Driver and you need to download it and put it in ``jars`` folder of your spark installation path. I download postgresql-42.1.1.jar from the official website and put it in jars folder.

From ``.csv``
-------------

|comp|

.. code-block:: python

	# pd.DataFrame pandas_df: DataFrame pandas
	pandas_df = pd.read_csv('Advertising.csv')
	#rdd.DataFrame. spark_df: DataFrame spark
	spark_df = spark.read.csv(path='Advertising.csv',
	#                sep=',',
	#                encoding='UTF-8',
	#                comment=None,
	               header=True, 
	               inferSchema=True)


From ``.json``
--------------

Data from: http://api.luftdaten.info/static/v1/data.json

.. code-block:: python

	pandas_df = pd.read_json("data/data.json")
	spark_df = spark.read.json('data/data.json')

|pyc|

.. code-block:: python

	pandas_df[['id','timestamp']].head(4)
	#
	spark_df[['id','timestamp']].show(4)

|comp|

.. code-block:: python

                                                    +----------+-------------------+
                                                    |        id|          timestamp|
                id  timestamp                       +----------+-------------------+
    0	2994551481  2019-02-28 17:23:52             |2994551481|2019-02-28 17:23:52|
    1	2994551482  2019-02-28 17:23:52             |2994551482|2019-02-28 17:23:52|
    2	2994551483  2019-02-28 17:23:52             |2994551483|2019-02-28 17:23:52|
    3	2994551484  2019-02-28 17:23:52             |2994551484|2019-02-28 17:23:52|
                                                    +----------+-------------------+
                                                    only showing top 4 rows


First ``n`` Rows
++++++++++++++++


|pyc|

.. code-block:: python

	pandas_df.head(4)
	# 
	spark_df.show(4)

|comp|

.. code-block:: python

	                                        +-----+-----+---------+-----+
	                                        |   TV|Radio|Newspaper|Sales|
	      TV  Radio  Newspaper  Sales       +-----+-----+---------+-----+
	0  230.1   37.8       69.2   22.1       |230.1| 37.8|     69.2| 22.1|
	1   44.5   39.3       45.1   10.4       | 44.5| 39.3|     45.1| 10.4|
	2   17.2   45.9       69.3    9.3       | 17.2| 45.9|     69.3|  9.3|
	3  151.5   41.3       58.5   18.5       |151.5| 41.3|     58.5| 18.5|
	                                        +-----+-----+---------+-----+
	                                        only showing top 4 rows

Column Names
++++++++++++

|pyc|

.. code-block:: python

	pandas_df.columns
	#
	spark_df.columns

|comp|

.. code-block:: python

	Index(['TV', 'Radio', 'Newspaper', 'Sales'], dtype='object')
	['TV', 'Radio', 'Newspaper', 'Sales']


Data types
++++++++++

|pyc|

.. code-block:: python

	pandas_df.dtypes
	#
	spark_df.dtypes

|comp|

.. code-block:: python

	TV           float64			[('TV', 'double'),
	Radio        float64			 ('Radio', 'double'),
	Newspaper    float64			 ('Newspaper', 'double'),
	Sales        float64			 ('Sales', 'double')]
	dtype: object

Replace Data types
++++++++++++++++++

.. code-block:: python

	my_list = [('a', 2, 3),
	           ('b', 5, 6),
	           ('c', 8, 9),
	           ('a', 2, 3),
	           ('b', 5, 6),
	           ('c', 8, 9)]
	col_name = ['col1', 'col2', 'col3']


	pandas_df = pd.DataFrame(my_list,columns=col_name)
	spark_df = spark.createDataFrame(pandas_df)

	pandas_df.dtypes

.. code-block:: python

	col1    object
	col2     int64
	col3     int64
	dtype: object


|pyc|

.. code-block:: python

	d = {'col2': 'string','col3':'string'}
	pandas_df = pandas_df.astype({'col2': 'str','col3':'str'})
	spark_df = spark_df.select(*list(set(spark_df.columns)-set(d.keys())),
	               *(col(c[0]).astype(c[1]).alias(c[0]) for c in d.items()))

|comp|

.. code-block:: python

	col1    object
	col2    object           [('col1', 'string'), ('col2', 'string'), ('col3', 'string')]
	col3    object
	dtype: object



Fill Null
+++++++++

.. code-block:: python

	my_list = [['a', 1, None], ['b', 2, 3],['c', 3, 4]]
	pandas_df = pd.DataFrame(my_list,columns=['A', 'B', 'C'])
	spark_df = spark.createDataFrame(my_list, ['A', 'B', 'C'])
	#
	pandas_df.head()
	spark_df.show()

|comp|

.. code-block:: python

	                  			+------+---+----+
	                  			|     A|  B|   C|
	        A  B    C 			+------+---+----+
	0    male  1  NaN 			|  male|  1|null|
	1  female  2  3.0 			|female|  2|   3|
	2    male  3  4.0 			|  male|  3|   4|
	                  			+------+---+----+


|pyc|

.. code-block:: python

	pandas_df.fillna(-99)
	#
	spark_df.fillna(-99).show()

|comp|

.. code-block:: python

	                  			+------+---+----+
	                  			|     A|  B|   C|
	        A  B    C 			+------+---+----+
	0    male  1  -99 			|  male|  1| -99|
	1  female  2  3.0 			|female|  2|   3|
	2    male  3  4.0 			|  male|  3|   4|
	                  			+------+---+----+

Replace Values
++++++++++++++

|pyc|

.. code-block:: python

	# caution: you need to chose specific col
	pandas_df.A.replace(['male', 'female'],[1, 0], inplace=True)
	pandas_df
	#caution: Mixed type replacements are not supported
	spark_df.na.replace(['male','female'],['1','0']).show()


|comp|

.. code-block:: python

	             			+---+---+----+
	             			|  A|  B|   C|
	   A  B    C 			+---+---+----+
	0  1  1  NaN 			|  1|  1|null|
	1  0  2  3.0 			|  0|  2|   3|
	2  1  3  4.0 			|  1|  3|   4|
	             			+---+---+----+

Rename Columns
++++++++++++++

Rename all columns
------------------

|pyc|

.. code-block:: python

	pandas_df.columns = ['a','b','c','d']
	pandas_df.head(4)
	#
	spark_df.toDF('a','b','c','d').show(4)


|comp|

.. code-block:: python

	                           			+-----+----+----+----+
	                           			|    a|   b|   c|   d|
	       a     b     c     d 			+-----+----+----+----+
	0  230.1  37.8  69.2  22.1 			|230.1|37.8|69.2|22.1| 
	1   44.5  39.3  45.1  10.4 			| 44.5|39.3|45.1|10.4|
	2   17.2  45.9  69.3   9.3 			| 17.2|45.9|69.3| 9.3|
	3  151.5  41.3  58.5  18.5 			|151.5|41.3|58.5|18.5|
	                           			+-----+----+----+----+
	                           			only showing top 4 rows

Rename one or more columns
--------------------------

.. code-block:: python

	mapping = {'Newspaper':'C','Sales':'D'}


|pyc|

.. code-block:: python

	pandas_df.rename(columns=mapping).head(4)
	#
	new_names = [mapping.get(col,col) for col in spark_df.columns]
	spark_df.toDF(*new_names).show(4)

|comp|

.. code-block:: python

	                            		+-----+-----+----+----+
	                            		|   TV|Radio|   C|   D|
	      TV  Radio     C     D 		+-----+-----+----+----+
	0  230.1   37.8  69.2  22.1 		|230.1| 37.8|69.2|22.1|
	1   44.5   39.3  45.1  10.4 		| 44.5| 39.3|45.1|10.4|
	2   17.2   45.9  69.3   9.3 		| 17.2| 45.9|69.3| 9.3|
	3  151.5   41.3  58.5  18.5 		|151.5| 41.3|58.5|18.5|
	                            		+-----+-----+----+----+
	                            		only showing top 4 rows

.. note::

	You can also use ``withColumnRenamed`` to rename one column in PySpark.

	|pyc|

	.. code-block:: python

		spark_df.withColumnRenamed('Newspaper','Paper').show(4

	|comp|

	.. code-block:: python

		+-----+-----+-----+-----+
		|   TV|Radio|Paper|Sales|
		+-----+-----+-----+-----+
		|230.1| 37.8| 69.2| 22.1|
		| 44.5| 39.3| 45.1| 10.4|
		| 17.2| 45.9| 69.3|  9.3|
		|151.5| 41.3| 58.5| 18.5|
		+-----+-----+-----+-----+
		only showing top 4 rows

Drop Columns
++++++++++++

.. code-block:: python

	drop_name = ['Newspaper','Sales']


|pyc|

.. code-block:: python

	pandas_df.drop(drop_name,axis=1).head(4)
	#
	spark_df.drop(*drop_name).show(4)

|comp|

.. code-block:: python

	                		+-----+-----+
	                		|   TV|Radio|
	      TV  Radio 		+-----+-----+
	0  230.1   37.8 		|230.1| 37.8|
	1   44.5   39.3 		| 44.5| 39.3|
	2   17.2   45.9 		| 17.2| 45.9|
	3  151.5   41.3 		|151.5| 41.3|
	                		+-----+-----+
	                		only showing top 4 rows

Filter
++++++

.. code-block:: python

	pandas_df = pd.read_csv('Advertising.csv')
	#
	spark_df = spark.read.csv(path='Advertising.csv',
	                    header=True, 
	                    inferSchema=True)

|pyc|

.. code-block:: python

	pandas_df[pandas_df.Newspaper<20].head(4)
	#
	spark_df[spark_df.Newspaper<20].show(4)


|comp|

.. code-block:: python

	                                		+-----+-----+---------+-----+
	                                		|   TV|Radio|Newspaper|Sales|
	       TV  Radio  Newspaper  Sales		+-----+-----+---------+-----+
	7   120.2   19.6       11.6   13.2		|120.2| 19.6|     11.6| 13.2|		 
	8     8.6    2.1        1.0    4.8		|  8.6|  2.1|      1.0|  4.8|
	11  214.7   24.0        4.0   17.4		|214.7| 24.0|      4.0| 17.4|
	13   97.5    7.6        7.2    9.7		| 97.5|  7.6|      7.2|  9.7|
	                                		+-----+-----+---------+-----+
	                                		only showing top 4 rows

|pyc|

.. code-block:: python

	pandas_df[(pandas_df.Newspaper<20)&(pandas_df.TV>100)].head(4)
	#
	spark_df[(spark_df.Newspaper<20)&(spark_df.TV>100)].show(4)

|comp|

.. code-block:: python

	                                		+-----+-----+---------+-----+
	                                		|   TV|Radio|Newspaper|Sales|
	       TV  Radio  Newspaper  Sales		+-----+-----+---------+-----+
	7   120.2   19.6       11.6   13.2		|120.2| 19.6|     11.6| 13.2|
	11  214.7   24.0        4.0   17.4		|214.7| 24.0|      4.0| 17.4|
	19  147.3   23.9       19.1   14.6		|147.3| 23.9|     19.1| 14.6|
	25  262.9    3.5       19.5   12.0		|262.9|  3.5|     19.5| 12.0|
	                                		+-----+-----+---------+-----+
	                                		only showing top 4 rows


With New Column
+++++++++++++++

|pyc|

.. code-block:: python

	pandas_df['tv_norm'] = pandas_df.TV/sum(pandas_df.TV)
	pandas_df.head(4)
	#
	spark_df.withColumn('tv_norm', spark_df.TV/spark_df.groupBy().agg(F.sum("TV")).collect()[0][0]).show(4)

|comp|

.. code-block:: python

	                                        	+-----+-----+---------+-----+--------------------+
	                                        	|   TV|Radio|Newspaper|Sales|             tv_norm|
	      TV  Radio  Newspaper  Sales   tv_norm	+-----+-----+---------+-----+--------------------+
	0  230.1   37.8       69.2   22.1  0.007824	|230.1| 37.8|     69.2| 22.1|0.007824268493802813|
	1   44.5   39.3       45.1   10.4  0.001513	| 44.5| 39.3|     45.1| 10.4|0.001513167961643...|
	2   17.2   45.9       69.3    9.3  0.000585	| 17.2| 45.9|     69.3|  9.3|5.848649200061207E-4|
	3  151.5   41.3       58.5   18.5  0.005152	|151.5| 41.3|     58.5| 18.5|0.005151571824472517|
	                                        	+-----+-----+---------+-----+--------------------+
	                                        	only showing top 4 rows

|pyc|

.. code-block:: python

	pandas_df['cond'] = pandas_df.apply(lambda c: 1 if ((c.TV>100)&(c.Radio<40)) else 2 if c.Sales> 10 else 3,axis=1)
	#
	spark_df.withColumn('cond',F.when((spark_df.TV>100)&(spark_df.Radio<40),1)\
	                      .when(spark_df.Sales>10, 2)\
	                      .otherwise(3)).show(4)

|comp|

.. code-block:: python

	                                        	+-----+-----+---------+-----+----+
	                                        	|   TV|Radio|Newspaper|Sales|cond|
	      TV  Radio  Newspaper  Sales  cond 	+-----+-----+---------+-----+----+
	0  230.1   37.8       69.2   22.1     1 	|230.1| 37.8|     69.2| 22.1|   1|	
	1   44.5   39.3       45.1   10.4     2 	| 44.5| 39.3|     45.1| 10.4|   2|	
	2   17.2   45.9       69.3    9.3     3 	| 17.2| 45.9|     69.3|  9.3|   3|	
	3  151.5   41.3       58.5   18.5     2 	|151.5| 41.3|     58.5| 18.5|   2|	
	                                        	+-----+-----+---------+-----+----+
	                                        	only showing top 4 rows

|pyc|

.. code-block:: python

	pandas_df['log_tv'] = np.log(pandas_df.TV)
	pandas_df.head(4)
	#
	spark_df.withColumn('log_tv',F.log(spark_df.TV)).show(4)

|comp|

.. code-block:: python

	                                            	+-----+-----+---------+-----+------------------+
	                                            	|   TV|Radio|Newspaper|Sales|            log_tv|
	      TV  Radio  Newspaper  Sales    log_tv 	+-----+-----+---------+-----+------------------+
	0  230.1   37.8       69.2   22.1  5.438514 	|230.1| 37.8|     69.2| 22.1|  5.43851399704132|
	1   44.5   39.3       45.1   10.4  3.795489 	| 44.5| 39.3|     45.1| 10.4|3.7954891891721947|
	2   17.2   45.9       69.3    9.3  2.844909 	| 17.2| 45.9|     69.3|  9.3|2.8449093838194073|
	3  151.5   41.3       58.5   18.5  5.020586 	|151.5| 41.3|     58.5| 18.5| 5.020585624949423|
	                                            	+-----+-----+---------+-----+------------------+
	                                            	only showing top 4 rows

|pyc|

.. code-block:: python

	pandas_df['tv+10'] = pandas_df.TV.apply(lambda x: x+10)
	pandas_df.head(4)
	#
	spark_df.withColumn('tv+10', spark_df.TV+10).show(4)

|comp|

.. code-block:: python

	                                         	+-----+-----+---------+-----+-----+
	                                         	|   TV|Radio|Newspaper|Sales|tv+10|
	      TV  Radio  Newspaper  Sales  tv+10 	+-----+-----+---------+-----+-----+
	0  230.1   37.8       69.2   22.1  240.1 	|230.1| 37.8|     69.2| 22.1|240.1|
	1   44.5   39.3       45.1   10.4   54.5 	| 44.5| 39.3|     45.1| 10.4| 54.5|
	2   17.2   45.9       69.3    9.3   27.2 	| 17.2| 45.9|     69.3|  9.3| 27.2|
	3  151.5   41.3       58.5   18.5  161.5 	|151.5| 41.3|     58.5| 18.5|161.5|
	                                         	+-----+-----+---------+-----+-----+
	                                         	only showing top 4 rows

Join
++++

.. code-block:: python

	leftp = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
	                    'B': ['B0', 'B1', 'B2', 'B3'],
	                    'C': ['C0', 'C1', 'C2', 'C3'],
	                    'D': ['D0', 'D1', 'D2', 'D3']},
	                    index=[0, 1, 2, 3])
	                    
	rightp = pd.DataFrame({'A': ['A0', 'A1', 'A6', 'A7'],
	                       'F': ['B4', 'B5', 'B6', 'B7'],
	                       'G': ['C4', 'C5', 'C6', 'C7'],
	                       'H': ['D4', 'D5', 'D6', 'D7']},
	                       index=[4, 5, 6, 7])

	lefts = spark.createDataFrame(leftp)  
	rights = spark.createDataFrame(rightp)

.. code-block:: python

	    A   B   C   D 		    A   F   G   H
	0  A0  B0  C0  D0 		4  A0  B4  C4  D4
	1  A1  B1  C1  D1 		5  A1  B5  C5  D5
	2  A2  B2  C2  D2 		6  A6  B6  C6  D6
	3  A3  B3  C3  D3 		7  A7  B7  C7  D7

Left Join
---------

|pyc|

.. code-block:: python

	leftp.merge(rightp,on='A',how='left')
	#
	lefts.join(rights,on='A',how='left')
	     .orderBy('A',ascending=True).show()

|comp|

.. code-block:: python

	                                	+---+---+---+---+----+----+----+
	                                	|  A|  B|  C|  D|   F|   G|   H|
	    A   B   C   D    F    G    H 	+---+---+---+---+----+----+----+
	0  A0  B0  C0  D0   B4   C4   D4 	| A0| B0| C0| D0|  B4|  C4|  D4|
	1  A1  B1  C1  D1   B5   C5   D5 	| A1| B1| C1| D1|  B5|  C5|  D5|
	2  A2  B2  C2  D2  NaN  NaN  NaN 	| A2| B2| C2| D2|null|null|null|
	3  A3  B3  C3  D3  NaN  NaN  NaN 	| A3| B3| C3| D3|null|null|null|
	                                	+---+---+---+---+----+----+----+

Right Join
----------

|pyc|

.. code-block:: python

	leftp.merge(rightp,on='A',how='right')
	#
	lefts.join(rights,on='A',how='right')
	     .orderBy('A',ascending=True).show()


|comp|

.. code-block:: python

	                                	+---+----+----+----+---+---+---+
	                                	|  A|   B|   C|   D|  F|  G|  H|
	    A    B    C    D   F   G   H 	+---+----+----+----+---+---+---+
	0  A0   B0   C0   D0  B4  C4  D4 	| A0|  B0|  C0|  D0| B4| C4| D4|
	1  A1   B1   C1   D1  B5  C5  D5 	| A1|  B1|  C1|  D1| B5| C5| D5|
	2  A6  NaN  NaN  NaN  B6  C6  D6 	| A6|null|null|null| B6| C6| D6|
	3  A7  NaN  NaN  NaN  B7  C7  D7 	| A7|null|null|null| B7| C7| D7|
	                                	+---+----+----+----+---+---+---+

Inner Join
----------

|pyc|

.. code-block:: python

	leftp.merge(rightp,on='A',how='inner')
	#
	lefts.join(rights,on='A',how='inner')
	     .orderBy('A',ascending=True).show()

|comp|

.. code-block:: python

	                            	+---+---+---+---+---+---+---+
	                            	|  A|  B|  C|  D|  F|  G|  H|
	    A   B   C   D   F   G   H 	+---+---+---+---+---+---+---+
	0  A0  B0  C0  D0  B4  C4  D4 	| A0| B0| C0| D0| B4| C4| D4|
	1  A1  B1  C1  D1  B5  C5  D5 	| A1| B1| C1| D1| B5| C5| D5|
	                            	+---+---+---+---+---+---+---+

Full Join
----------

|pyc|

.. code-block:: python

	leftp.merge(rightp,on='A',how='full')
	#
	lefts.join(rights,on='A',how='full')
	     .orderBy('A',ascending=True).show()

|comp|

.. code-block:: python

	                                    	+---+----+----+----+----+----+----+
	                                    	|  A|   B|   C|   D|   F|   G|   H|
	    A    B    C    D    F    G    H 	+---+----+----+----+----+----+----+
	0  A0   B0   C0   D0   B4   C4   D4 	| A0|  B0|  C0|  D0|  B4|  C4|  D4|
	1  A1   B1   C1   D1   B5   C5   D5 	| A1|  B1|  C1|  D1|  B5|  C5|  D5|
	2  A2   B2   C2   D2  NaN  NaN  NaN 	| A2|  B2|  C2|  D2|null|null|null|
	3  A3   B3   C3   D3  NaN  NaN  NaN 	| A3|  B3|  C3|  D3|null|null|null|
	4  A6  NaN  NaN  NaN   B6   C6   D6 	| A6|null|null|null|  B6|  C6|  D6|
	5  A7  NaN  NaN  NaN   B7   C7   D7 	| A7|null|null|null|  B7|  C7|  D7|
	                                    	+---+----+----+----+----+----+----+


Concat Columns
++++++++++++++

.. code-block:: python

	my_list = [('a', 2, 3),
	           ('b', 5, 6),
	           ('c', 8, 9),
	           ('a', 2, 3),
	           ('b', 5, 6),
	           ('c', 8, 9)]
	col_name = ['col1', 'col2', 'col3']
	#
	pandas_df = pd.DataFrame(my_list,columns=col_name)
	spark_df = spark.createDataFrame(my_list,schema=col_name)

.. code-block:: python

	  col1  col2  col3
	0    a     2     3
	1    b     5     6
	2    c     8     9
	3    a     2     3
	4    b     5     6
	5    c     8     9

|pyc|

.. code-block:: python

	pandas_df['concat'] = pandas_df.apply(lambda x:'%s%s'%(x['col1'],x['col2']),axis=1)
	pandas_df
	#
	spark_df.withColumn('concat',F.concat('col1','col2')).show()

|comp|

.. code-block:: python

	                        		+----+----+----+------+
	                        		|col1|col2|col3|concat|
	  col1  col2  col3 concat 		+----+----+----+------+
	0    a     2     3     a2 		|   a|   2|   3|    a2|
	1    b     5     6     b5 		|   b|   5|   6|    b5|
	2    c     8     9     c8 		|   c|   8|   9|    c8|
	3    a     2     3     a2 		|   a|   2|   3|    a2|
	4    b     5     6     b5 		|   b|   5|   6|    b5|
	5    c     8     9     c8 		|   c|   8|   9|    c8|
	                        		+----+----+----+------+

GroupBy
+++++++

|pyc|

.. code-block:: python

	pandas_df.groupby(['col1']).agg({'col2':'min','col3':'mean'})
	#
	spark_df.groupBy(['col1']).agg({'col2': 'min', 'col3': 'avg'}).show()

|comp|

.. code-block:: python

	                			+----+---------+---------+
	      col2  col3 			|col1|min(col2)|avg(col3)|
	col1             			+----+---------+---------+
	a        2     3 			|   c|        8|      9.0|
	b        5     6 			|   b|        5|      6.0|
	c        8     9 			|   a|        2|      3.0|
	                			+----+---------+---------+

Pivot
+++++

|pyc|

.. code-block:: python

	pd.pivot_table(pandas_df, values='col3', index='col1', columns='col2', aggfunc=np.sum)
	#
	spark_df.groupBy(['col1']).pivot('col2').sum('col3').show()

|comp|

.. code-block:: python

	                    		+----+----+----+----+
	col2    2     5     8 		|col1|   2|   5|   8|	
	col1                  		+----+----+----+----+
	a     6.0   NaN   NaN 		|   c|null|null|  18|
	b     NaN  12.0   NaN 		|   b|null|  12|null|
	c     NaN   NaN  18.0 		|   a|   6|null|null|
	                    		+----+----+----+----+


Unixtime to Date
++++++++++++++++

.. code-block:: python

	from datetime import datetime

	my_list = [['a', int("1284101485")], ['b', int("2284101485")],['c', int("3284101485")]]
	col_name = ['A', 'ts']

	pandas_df = pd.DataFrame(my_list,columns=col_name)
	spark_df = spark.createDataFrame(pandas_df)


|pyc|

.. code-block:: python

	pandas_df['datetime'] = pd.to_datetime(pandas_df['ts'], unit='s').dt.tz_localize('UTC')
	pandas_df

	spark.conf.set("spark.sql.session.timeZone", "UTC")
	from pyspark.sql.types import DateType
	spark_df.withColumn('date', F.from_unixtime('ts')).show() #.cast(DateType())


|comp|

.. code-block:: python

	                                        	+---+----------+-------------------+
	                                        	|  A|        ts|               date|
	   A          ts                  datetime 	+---+----------+-------------------+
	0  a  1284101485 2010-09-10 06:51:25+00:00 	|  a|1284101485|2010-09-10 06:51:25|
	1  b  2284101485 2042-05-19 08:38:05+00:00 	|  b|2284101485|2042-05-19 08:38:05|
	2  c  3284101485 2074-01-25 10:24:45+00:00 	|  c|3284101485|2074-01-25 10:24:45|
	                                        	+---+----------+-------------------+





