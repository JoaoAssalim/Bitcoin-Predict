import streamlit as st
from model import model
from model_page import model_page
from predict_page import predict_page
from information import info
import webbrowser

def main():
    st.set_page_config(page_title="Bitcoin Predict Price", page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)
    menu = st.sidebar.selectbox(
        "Chosse the page",
        ("Project Informations", "View model", "Try prediction")
    )

    if st.sidebar.button("Repository", use_container_width=True):
        webbrowser.open_new_tab("https://github.com/JoaoAssalim/Bitcoin-Predict")

    if menu == "View model":
        model_page()
    elif menu == "Project Informations":
        info()
    else:
        predict_page()
        
main()