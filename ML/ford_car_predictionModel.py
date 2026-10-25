import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('ford.csv')
# numericOnly = [df['year' 'price' 'mileage' 'tax' 'mpg' 'engineSize']]
# aim - to check all the cols who are related to price by plotting different type of graphs between 'em

# year x price
# mileage x -price
# tax x price (Doubted)
# mpg x -price
# engineSize x price (Doubted)

# print(df.head())
print(df.describe(), df.shape)
# sns.heatmap(df.corr(numeric_only = True), annot=True)
sns.scatterplot(data = df, x = 'engineSize', y = 'price')

plt.show()