import streamlit as st
import pandas as pd

st.title('My first app')
df_reg = pd.read_csv("mumbai_houses_task.csv")


def main():
    # option to choose between
    select_page = st.sidebar.selectbox("Prediction or About", ("Predict", "About"), key="Select")

    if (select_page == "title page"):
        prediction_page()

    elif (select_page == "dataset description"):
        about()

    elif (select_page == "visualizations"):
        about()

    elif (select_page == "models predictions"):
        about()

    elif (select_page == "dimension reduction"):
        about()


# First page - prediction page
def prediction_page():
    st.header("РГР по машинному обучению студента группы ФИТ-222 Маркиной Екатерины Константиновны")


Prise = st.slider('Choose prise', min_value=0,
                  max_value=1000000000000000, value=(20, 50))
Area = st.slider('Choose area', min_value=0,
                 max_value=10000000, value=(20, 50))
Latitude = st.slider('Choose latitude', min_value=0,
                     max_value=1000000000000000, value=(20, 50))
Longitude = st.slider('Choose longitude', min_value=0,
                      max_value=1000000000000000, value=(20, 50))

Bedrooms = st.multiselect('Choose bedrooms', df_reg['bedrooms'].unique())
Bathrooms = st.multiselect('Choose bathrooms', df_reg['bathrooms'].unique())
Balconyv = st.multiselect('Choose balconyv', df_reg['balconyv'].unique())
Status = st.multiselect('Choose status', df_reg['status'].unique())
Neworold = st.multiselect('Choose neworold', df_reg['neworold'].unique())
Parking = st.multiselect('Choose parking', df_reg['parking'].unique())
Furnished_status = st.multiselect(
    'Choose furnished_status', df_reg['furnished_status'].unique())
Lift = st.multiselect('Choose lift', df_reg['lift'].unique())
Type_of_building = st.multiselect(
    'Choose type_of_building', df_reg['type_of_building'].unique())


# Second page - about page
def about():
    st.header("About this model")


main()
