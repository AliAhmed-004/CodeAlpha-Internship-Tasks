# -*- coding: utf-8 -*-
"""Linear Regression Model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11WZ6VJB9Jir1qDNI5oz7FbnhevXBhv6S

# Predicting Median value of owner-occupied homes in $1000s (medv) From "Boston Housing Dataset"

# Importing Libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""# Creating Dataframe of Dataset"""

data = pd.read_csv('BostonHousing.csv')

data.head()

"""# Creating a heatmap to see which values affect the 'medv' column the most"""

import seaborn as sns

sns.heatmap(data.corr(), cmap='Reds')

"""# Dropping Unnecessary Columns

From the heatmap, we can see that 'chas' have very little effect on 'medv' which is our target. Thus, we can safely discard this column.
"""

data.drop('chas', axis=1, inplace=True)

"""# Confirming the heatmap one last time"""

sns.heatmap(data.corr(), cmap='Reds')

"""# Checking Null Values"""

data.isnull().sum()

"""#Filling Null Values"""

data.fillna(method='ffill', inplace=True)

data.isnull().sum()

"""# Confirming all datatypes are numeric"""

data.info()

"""# Seperating Features and Target"""

X = data.drop('medv', axis=1)
y = data['medv']

"""# Creating Testing and Training Data"""

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

"""# Creating Model"""

from sklearn.linear_model import LinearRegression

model = LinearRegression()

"""# Training Model"""

model.fit(X_train, y_train)

"""# Making Predictions"""

predictions = model.predict(X_test)

"""# Plotting the Predictions for Visualization
In the graph, the red line is the actual values while the blue dots are the predictions
"""

plt.figure(figsize=(10, 6))
plt.scatter(y_test, predictions, color='blue', alpha=0.6)
plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', linestyle='--', linewidth=2)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual(Red Line) vs Predicted(Blue Dots) Values')
plt.grid(True)

"""# Evaluating the Model"""

from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

"""# Conclusion:
From the visualization, we can see that the predictions that the model made are not perfect, but it is still reasonable since the values do not deviate from the actual values too much.
"""