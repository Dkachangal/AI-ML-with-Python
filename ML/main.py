import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv('Salary_dataset.csv', index_col=0)

# print(df.isnull().sum())

# print(df.describe())

# x = df[df['YearsExperience'] > 3]
# y = df['Salary'].mean()
# print(x)
# print("mean salary : ", y)
x = df[['YearsExperience']]
y = df['Salary']


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# print(x_test)
print(y_test)

# creating a model
model = LinearRegression()
model.fit(x_train, y_train)

age = [[8.5]]
prediction = model.predict(x_test)

plt.scatter(x, y)
plt.plot(x, model.predict(x), color='red',label='regression')
plt.legend()
print(prediction)
print(y_test)
plt.show()