import pandas as pd

d = {'A': [1, 0, None, 3],
     'B': [1, 0, 0, 0],
     'C': [4, None, 7, 8]}

df = pd.DataFrame(d)
print(df)

# fill missing numerical value with 0
print(df.fillna(0))

# fill missing numerical value with mean
df = df.fillna(df.mean())
print(df)