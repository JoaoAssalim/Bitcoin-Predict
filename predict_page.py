import streamlit as st
from model import model
from streamlit_extras.let_it_rain import rain

def predict_page():
    #Low=0, Open=0, High=0, Volume=0, Marketcap=0
    st.title('Try Model')

    low_value = st.text_input(
        "Enter the Low Value of the Day",
        placeholder="Low Value",
    )

    high_value = st.text_input(
        "Enter the High Value of the Day",
        placeholder="High Value",
    )

    open_value = st.text_input(
        "Enter the Open Value of the Day",
        placeholder="Open Value",
    )

    volume_value = st.text_input(
        "Enter the Volume Value of the Day",
        placeholder="Volume Value",
    )

    marketcap_value = st.text_input(
        "Enter the Volume Marketcap of the Day",
        placeholder="Volume Marketcap",
    )

    predict = st.button('Predict')

    if predict:
        if low_value and high_value and open_value and volume_value and marketcap_value:
            predict = model("predict", low_value, open_value, high_value, volume_value, marketcap_value)
            st.dataframe(predict, use_container_width=True, hide_index=True)
            rain(
                emoji="🎈",
                font_size=54,
                falling_speed=7,
                animation_length="short",
            )
        else:
            st.error(' Missing Values')