import streamlit as st
from .menu import menu


def init_page():
    st.set_page_config(
        page_title="Shabi",
        page_icon="🍌",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    menu()
