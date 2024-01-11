import streamlit as st
import pandas as pd
st.title('My first app')
df_class = pd.read_csv("mumbai_houses_task.csv")
Location = st.multiselect('Choose location', df_class['location'].unique())
Min_temp = st.radio('Choose a min_temp', df_class['min_temp'].unique())
Max_temp = st.radio('Choose a max_temp', df_class['max_temp'].unique())
Rainfall = st.radio('Choose a rainfall', df_class['rainfall'].unique())
Evaporation = st.radio('Choose a evaporation', df_class['evaporation'].unique())
Sunshine = st.radio('Choose a sunshine', df_class['sunshine'].unique())
WindGustDir = st.radio('Choose a wind_gust_dir', df_class['wind_gust_dir'].unique())
WindGustSpeed = st.radio('Choose a wind_gust_speed', df_class['wind_gust_speed'].unique())
WindGustSpeed = st.radio('Choose a wind_gust_dir', df_class['wind_gust_dir'].unique())
WindGustSpeed = st.radio('Choose a wind_gust_dir', df_class['wind_gust_dir'].unique())
WindGustSpeed = st.radio('Choose a wind_gust_dir', df_class['wind_gust_dir'].unique())
WindGustSpeed = st.radio('Choose a wind_gust_dir', df_class['wind_gust_dir'].unique())






new_df = df_class[(df_class['region'].isin(Region)) & (df_class['smoker'].isin(Smoker)) & (df_class['sex'] =
= Sex)
 & (df_class['age']> Age[0]) & (df_class['age']< Age[1])
 & (df_class['children'] == Children)]
st.write(new_df)

