import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('My first app using streamlit')
st.write('## Hello, *World!* :sunglasses:')
#username = st.text_input('Enter your name')
#st.write(f"Hi {username} Here's our first attempt at using data to create a table:")
#st.write(pd.DataFrame({ 'first column': [1, 2, 3, 4], 'second column': [10, 20, 30, 40] }))
x = st.text_input("Movie", "Star Wars")
if st.button("Click Me"):
    st.write(f"Your favorite movie is `{x}`")

data = pd.read_csv("movies.csv")
st.write(data)
st.write(data.describe())
st.write(data.columns)

fig, ax = plt.subplots()
ax.hist(data['runtime'], bins=20)
st.pyplot(fig)