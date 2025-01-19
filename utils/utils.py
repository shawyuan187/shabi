import streamlit as st
from .menu import menu


def init_page():
    st.set_page_config(
        page_title="Shabi",
        page_icon="🍌",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Add custom CSS for modern title styling
    st.markdown(
        """
        <style>
        .title-text {
            background: linear-gradient(45deg, #2196F3, #4CAF50);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-family: 'Helvetica Neue', sans-serif;
            font-weight: 700;
            font-size: 3em;
            text-align: left;
            margin-bottom: 1em;
            padding: 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        </style>
    """,
        unsafe_allow_html=True,
    )

    menu()


def set_title(title_text):
    st.markdown(f'<h1 class="title-text">{title_text}</h1>', unsafe_allow_html=True)
