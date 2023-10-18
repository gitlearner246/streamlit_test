import streamlit as st
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a decision tree classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Create a Streamlit app
st.title('Iris Species Prediction App')

# Create sliders for input features
sepal_length = st.slider('Sepal Length', min_value=4.0, max_value=8.0, value=5.0)
sepal_width = st.slider('Sepal Width', min_value=2.0, max_value=5.0, value=3.0)
petal_length = st.slider('Petal Length', min_value=1.0, max_value=7.0, value=4.0)
petal_width = st.slider('Petal Width', min_value=0.1, max_value=3.0, value=1.0)

# Predict the species of the iris
features = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = clf.predict(features)
st.subheader(f'The species of the iris is predicted to be: {iris.target_names[prediction][0]}')
