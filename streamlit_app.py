import streamlit as st

# split the code into different functions for each page

def main():

    # option to choose between 
    select_page = st.sidebar.selectbox("Prediction or About", ("Predict", "About"), key = "Select")
    
    # if user selects Predict page
    if (select_page == "Predict"):
        prediction_page()
    
    # if user selects About page
    elif (select_page == "About"):
        about()


# First page - prediction page
def prediction_page():
    st.header("Interactive Diabetes Web Application")

    Age = st.slider("Age", 0, 100)

    st.write("Selected age is " + str(Age))

    Question = st.selectbox("Select Answer", ("Yes", "No"), key = "answer")
    if (Question == "Yes"):
        st.write("You selected " + Question)

    elif (Question == "No"):
        st.write("You selected " + Question)

    value = ''
    checkbox_one = st.checkbox("Did Excercise")
    checkbox_two = st.checkbox("Did not Exercise")

    if (checkbox_one):
      value = "Did Excercise"
      
    else:
      value = "Did not Excercise"
      
    st.write(f"You {value}")
    
    
# Second page - about page
def about():
    st.header("About this model")


main()