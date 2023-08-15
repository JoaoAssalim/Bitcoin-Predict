import streamlit as st
from model import model

def model_page():
    st.title('Predicting Bitcoin Price with Machine Learning')

    st.subheader("Getting Data")
    df = model("get_database")
    st.dataframe(df)

    st.subheader("Pre processing Data")
    st.write("Data Normalized")
    pre_df = model("pre_processing_data")
    st.dataframe(pre_df)

    st.subheader("Model Prediction")
    st.write("To make this machine learning model, we used Decision Tree Regressor model")

    predict_df = model("database_predict")
    st.dataframe(predict_df)

    score = model("model_score")*100
    st.metric(label="Model Accuracy", value=f'{score:.2f}%')