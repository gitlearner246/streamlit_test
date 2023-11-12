import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import time

# Load data
data = pd.read_csv('Salary_Data.csv')
X = data.iloc[:, :-1].values 
y = data.iloc[:, -1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Create a linear regression object
from sklearn.linear_model import LinearRegression
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Get the slope and intercept of the line
slope = model.coef_[0]
intercept = model.intercept_

# Create a function to predict y from x
def predict(x):
    return slope * x + intercept

# Create a Streamlit app
st.title('Simple Linear Regression Example')
st.write('This app demonstrates how to perform simple linear regression using Python and Streamlit.')

# Add a slider for the user to input x
x = st.slider('Input x:', 0, 100)

x = st.number_input('Insert a number', step=1)
st.write('The current number is ', x)

# Predict y from x and display the result
y = predict(x)
st.write(f'Predicted y: {y:.2f}')


# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(1.5)
    st.success("Done!")