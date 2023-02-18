import streamlit as st
import numpy as np
import pandas as pd


st.title('Streamlit 超入門')#タイトルの追加

st.write('DateFeame')#文や画像、表の表示

"""
df = pd.DataFrame({
    '1列目': [1,2,3,4],
    '2列目': [10,20,30,40]
})

st.write(df)#表の表示。引数は表示させたいデータフレーム

st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)#動的な表。表の縦横を調節可能。style.highlight_max(axis=0)で最大値をハイライトaxis0で列1で行
st.table(df)#静的な表

df = pd.DataFrame(
    np.random.rand(20,3),#（列,行）
    columns=['a','b','c']
)

st.line_chart(df)#グラフ表示

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon',]#緯度経度
)
st.map(df)#地図上に座標表示

st.write('Display Image')

img=Image.open('sample.jpg')#画像表示
st.image(img, caption='sample',use_column_width=True)

if st.checkbox('show image'):#チェックボックス
   img=Image.open('sample.jpg')
   st.image(img, caption='sample',use_column_width=True)
"""
option=st.selectbox(
    '好きな数字を教えて',#ラベル
    list(range(1,11))#オプション
)



