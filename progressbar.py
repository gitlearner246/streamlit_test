import pandas as pd
from PIL import Image
import streamlit as st
import time

st.write('display progressbar')
"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f"iteration {i+1}")
  bar.progress(i+1)
  time.sleep(0.1)