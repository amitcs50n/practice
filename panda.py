import pandas as pd

# s = pd.Series([10, 20, 30], index=["a", "b", "c"])
# print(s)


data = {"name": ["amit", "Rinku"], "Age": [20, 30]}
df = pd.DataFrame(data)
#print(df)
#print(df["name"])
print(df[['name', 'Age']]) # Multiple column