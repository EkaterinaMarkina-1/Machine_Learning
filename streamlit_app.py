import streamlit as st
import pandas as pd
st.title('My first app')
df_class = pd.read_csv("weatherAUS.csv")
Region = st.multiselect('Choose regions', df_class['region'].unique())
Smoker = st.multiselect('Choose smoker', df_class['smoker'].unique())
Sex = st.radio('Choose a gender', df_class['sex'].unique())
Age = st.slider('Choose age', min_value=17, max_value=66, value=(20, 50))
Children = st.number_input('Choose the number of children', min_value= 0,
 max_value=5, value =1, step=1)
new_df = df_class[(df_class['region'].isin(Region)) & (df_class['smoker'].isin(Smoker)) & (df_class['sex'] =
= Sex)
 & (df_class['age']> Age[0]) & (df_class['age']< Age[1])
 & (df_class['children'] == Children)]
st.write(new_df)

