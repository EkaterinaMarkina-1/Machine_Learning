import streamlit as st
import pandas as pd
st.title('My first app')
df = pd.read_csv("weatherAUS.csv")
st.write(df)
