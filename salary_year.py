import streamlit as st
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
import pandas as pd

# Assuming X and y are your features and labels
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
print(y.shape)

# Fit a decision tree regressor
regressor = DecisionTreeRegressor()
regressor.fit(X, y)

# Generate a grid of points
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))

# Create the scatter plot and line plot
fig, ax = plt.subplots()
ax.scatter(X, y, color='red')
ax.plot(X_grid, regressor.predict(X_grid), color='blue')
ax.set_title('Truth or Bluff (Decision Tree Regression)')
ax.set_xlabel('Position level')
ax.set_ylabel('Salary')

# Display the plot with Streamlit
st.pyplot(fig)
