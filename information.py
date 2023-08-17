import streamlit as st

def info():
    st.header("Project Informations")

    st.subheader("DataSet")
    st.write("The dataset was found on kaggle (is a data science competition platform and online community of data scientists and machine learning practitioners under Google LLC) .")

    st.subheader("What's Pre Processing?")
    st.write("Pre processing is an initial step for a model, so you remove information that will not be valid, clean the data and standardize it.")

    st.subheader("What's a machine learning model and witch was used?")
    st.write("A machine learning model is a means of organizing and training your data to better predict some value, we have many machine learning models, each with its own specialty and for each need you must study and analyze which model is best for your problem.")
    st.write("For this project, the Decision Tree Regressor model was used.")

    st.subheader("What's Decision Tree Regressor?")
    st.write("Decision trees is a type of supervised machine learning algorithm that is used by the Train Using AutoML tool and classifies or regresses the data using true or false answers to certain questions. The resulting structure, when visualized, is in the form of a tree with different types of nodes—root, internal, and leaf.")

    st.subheader("How Model Predict Works?")
    st.write("It uses the training performed with pre-processed data, and thus makes a regression to try to predict the value.")