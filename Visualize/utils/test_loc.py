import pandas as pd

# Creating a sample dataframe
data = pd.DataFrame({
    'age': [30, 20, 50],
    'height': [150, 160, 170],
    'weight': [70, 60, 65]
}, index=['Alice', 'Bob', 'Charlie'])

# Using loc to select a row by label
print(data.loc['Alice'])

# Using loc to select a column by label
print(data.loc[:, 'height'])

# Using loc to select a specific cell by row and column labels
print(data.loc['Bob', 'weight'])