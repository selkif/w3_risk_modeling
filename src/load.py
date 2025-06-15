import pandas as pd

# Load the data
df = pd.read_csv('../data/MachineLearningRating_v3.txt', sep='|')


df.to_csv('../data/insurance_data.csv', index=False)


print(df.head())
print(df.info())
print(df.describe())