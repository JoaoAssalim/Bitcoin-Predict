import streamlit as st
from model import model
from model_page import model_page
from predict_page import predict_page

def main():
    menu = st.sidebar.selectbox(
        "Chosse the page",
        ("View model", "Try prediction")
    )

    if menu == "View model":
        model_page()
    
    else:
        predict_page()
main()
