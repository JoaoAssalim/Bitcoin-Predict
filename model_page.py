import streamlit as st
from model import model

def model_page():
    st.title('Predicting Bitcoin Price with Machine Learning')

    st.subheader("Getting Data")
    df = model("get_database")
    st.dataframe(df, use_container_width=True)

    st.subheader("After Pre processing Data")
    pre_df = model("pre_processing_data")
    st.dataframe(pre_df, use_container_width=True)

    st.subheader("Model Prediction")

    predict_df = model("database_predict")
    st.dataframe(predict_df, use_container_width=True)

    score = model("model_score")
    st.progress(score, text=f"Model Accuracy: {score*100:.2f}%")