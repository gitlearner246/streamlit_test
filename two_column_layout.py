import pandas as pd
from PIL import Image
import streamlit as st

# カラム数:2
left_column, right_column = st.columns(2)
btn = left_column.button('右カラムに文字を表示')
if btn:
  right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# text = st.sidebar.text_input('What\'s your hobby?')
# st.write('Your hobby is', text)

# condition = st.sidebar.slider('How are you?', 0, 100, 50)
# 'condition', condition

