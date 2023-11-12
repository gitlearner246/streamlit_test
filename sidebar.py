import pandas as pd
from PIL import Image
import streamlit as st

text = st.sidebar.text_input('What\'s your hobby?')
st.write('Your hobby is', text)

condition = st.sidebar.slider('How are you?', 0, 100, 50)
'condition', condition

