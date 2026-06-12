import pandas as pd

data = {
    "ships": ["X1", "X2", "X3", "X4", "X5", "X6"],
    "port_entries": [2, 2, 4, 7, 4, 7]
}
df = pd.DataFrame(data)

print(df.head())
print(df.shape)
print(df.describe())

