import streamlit as st
import pandas as pd

data = {'Series_1': [1, 3, 4, 5, 7], 'Series_2': [10, 30, 40, 100, 250]}

df = pd.DataFrame(data)

st.title('Our streamlit app')
st.subheader('Introducing streamlith with automate everything with python')
st.write('''
This is our first web app.
Enjoy it.
''')

st.write(df)
