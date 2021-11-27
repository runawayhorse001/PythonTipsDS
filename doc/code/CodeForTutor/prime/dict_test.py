col_names = ['name', 'Age', 'Sex', 'Car']
col_values = ['Michael', '30', 'Male', ['Honda', 'Tesla']]


d = {key: value for key, value in zip(col_names, col_values)}
print(d)

import pandas as pd

df = pd.DataFrame(d)
print(df)


print([(key, val) for key, val in d.items()])


# get

data1 = d.get("name", "best")
data2 = d.get("names", "George")
print(data1)  # Michael
print(data2)  # Michael


# replace values in dict
replace = {'Car': ['Tesla S', 'Tesla X']}
print(d)
d.update(replace)
print(d)

# add key and values in dict
added = {'Kid': ['Tom', 'Jim']}
print(d)
d.update(added)
print(d)

# update keys in dict
mapping = {'Car': 'Cars', 'Kid': 'Kids'}
#
# print({replace[key]: value for key, value in d.items()})

# print([replace.get(key, key) for key in d])
print({mapping.get(key, key): val for key, val in d.items()})


