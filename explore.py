#Excercise 1 

import pandas as pd

df = pd.read_csv('data/retail_sales.csv')

print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)
print()

#excercise 2

south = df[df['region'] == 'South']

print(len(south))
print(south.head())
print()

#excercise 3

print(df.sort_values('revenue', ascending=False).head(5))
print()

#excercise 4

big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]

print(len(big_south))
print(big_south.head())