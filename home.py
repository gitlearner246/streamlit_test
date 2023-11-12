import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# マークダウン。markdown 又は write
st.markdown('*Markdown*')
st.write('**Text parsing**')

# HTMl 記述
import streamlit.components.v1 as components
components.html('''
<a href="http://sample.html">Link</a>
''')

# コードブロック
st.code('print("Hello World!")')

# エラーメッセージ。赤文字に薄赤背景
st.error('Error message')

# 警告メッセージ。黄色文字に薄黄色背景
st.warning('Warning message')

# 情報メッセージ。青文字に薄青背景
st.info('Information message')

# 成功メッセージ。緑文字に薄緑背景
st.success('Success message')

# 例外メッセージ。Exception部分が太字の赤文字・薄赤背景
st.exception(Exception('Ooops!'))

# 辞書型データ（JSON）の表示。各階層に折り畳み機能付
d = {
  'foo': 'bar',
  'users': [
    'alice',
    'bob',
  ],
}
st.json(d)

# 折り畳み表示
with st.expander('Expander title'):
  st.json(d)




# data = {
#     'x': np.random.random(20),
#     'y': np.random.random(20) - 0.5,
#     'z': np.random.random(20) - 1.0,
#     }
# df = pd.DataFrame(data)

# st.dataframe(df)
# st.table(df)



# 画像ファイルを直接指定する場合
# img = st.image('dog.jpg')



# df = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(df)



flgCheck_A = st.checkbox('Checkbox A')
flgCheck_B = st.checkbox('Checkbox B')

# チェックボックスのイベントは並列して発生する可能性があるため、
# elif を使用すろとイベントのキャッチ漏れに繋がる。
if flgCheck_A:
    st.text('Checkbox A has checked')
if flgCheck_B:
    st.text('Checkbox B has checked')



selected_item = st.radio(
                  'which Animal do you like?',
                  ['Dog', 'Cat']
                )

st.text(selected_item)



selected_item = st.selectbox('Select item', ['A', 'B', 'C'])

st.text(selected_item)

# デフォルト値を設定する場合は index オプションを設定する。
selected_item = st.multiselect('Select item', ['A', 'B', 'C'], default=['B', 'C'])

# 初期値が 1 なので B が表示される。
st.text(selected_item)



# 文字列の入力。第一引数は入力ボックス上部のラベル名
inputText_A = st.text_input('Input any words')

# 初期値を指定することも可能
inputText_B = st.text_input(label='Please input text', value='aaa')

# テキストエリアも使い方は同様
inputArea = st.text_area('Please input any strings', 'Place holder')


# 整数を入力させる場合
number = st.number_input('Input any number', 0)

# 小数値を入力させる場合
number = st.number_input('Input any number', 0.0)