import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


# Load data
data = pd.read_csv('50_Startups.csv')
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values




# Encoding Category Variable
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
X = np.array(ct.fit_transform(X))


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Create a linear regression object
from sklearn.linear_model import LinearRegression
model = LinearRegression()
# Training Model
model.fit(X_train, y_train)


# Predict test data
y_pred = model.predict(X_test)
np.set_printoptions(precision=2)


# 縦に変え、左が予測、右が実際の値
np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1)


# Get the coefficients and intercept of the line
coefficients = model.coef_
intercept = model.intercept_

# Create a function to predict y from x1 and x2
def predict(x1, x2, x3, x4):
    return coefficients[0] * x1 + coefficients[1] * x2 + coefficients[2] * x3 + coefficients[3] * x4 + intercept

# Create a Streamlit app
st.title('Multiple Linear Regression Example')
st.write('This app demonstrates how to perform multiple linear regression using Python and Streamlit.')

# Add sliders for the user to input x1 and x2
number = st.number_input('R&D Spend')
st.write('The current number is ', number)
x1 = number
number2 = st.number_input('Administration Spend')
st.write('The current number is ', number2)
x2 = number2
number3 = st.number_input('Marketing Spend')
st.write('The current number is ', number3)
x3 = number3

number4 = st.slider('1 - 4', 0, 4)
st.write('You selected:', number4)
x4 = number4


# Predict index_price from interest_rate and unemployment_rate and display the result
index_price = predict(x1, x2, x3, x4)
st.write(f'Predicted index price: {index_price:.2f}')
