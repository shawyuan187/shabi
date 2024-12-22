import streamlit as st
import os


def menu():
    st.sidebar.title("Menu")
    st.sidebar.page_link(page="main.py", label="Home", icon="🏠")

    st.sidebar.markdown("---")

    st.sidebar.title("class")
    pages_files_path = os.listdir("pages")
    pages_files_path = [page for page in pages_files_path if "adv" in page]
    page_path = st.sidebar.selectbox("選擇頁面", pages_files_path)
    if st.sidebar.button(f"go", key=f"go_to_page"):
        st.switch_page(f"pages/{page_path}")
