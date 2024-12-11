import pandas as pd

# Read the CSV file
data_2018 = pd.read_csv("data/2018.csv", header=1, encoding="cp949")

print(data_2018)

# pd.read_csv("data.csv", header=1)
