import pandas as pd

# s = pd.Series([10, 20, 30], index=["a", "b", "c"])
# print(s)


data = {"name": ["amit", "Rinku"], "Age": [20, 30]}
df = pd.DataFrame(data)
#print(df)
#print(df["name"])
# print(df[['name', 'Age']]) # Multiple column

#print(df.head())     # First 5 rows
 #df.tail()       # Last 5 rows
# print(df.shape)      # (rows, columns)
# df.info()       # Summary of data types and nulls
# print(df.describe())  # Stats summary


# df['name']              # Column
# df[['name', 'Age']]    # Multiple columns
# print(df.iloc[0])            # First row by position
# print()
# print(df.loc[0])           # First row by index label


df['Salary'] = [50000, 60000]  # Add new column
print(df)

