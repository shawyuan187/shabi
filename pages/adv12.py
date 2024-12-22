import streamlit as st
import os
from utils import init_page

init_page()
col1, col2 = st.columns([1, 2])
with col1:
    if st.button("按鈕1", key="btn8"):
        st.balloons()
    st.write("我是col1")
with col2:
    st.button("按鈕2", key="btn9")
    st.write("我是col2")
col_num = st.number_input("輸入數字", step=1, value=4)
cols = st.columns(col_num)
for i in range(col_num):
    with cols[i]:
        st.button(f"按鈕{i}", key=f"btn{i+10}")

col1, col2 = st.columns([1, 2])
with col1:
    st.button("按鈕1", key="1")
    st.button("按鈕2", key="2")
    st.button("按鈕3", key="3")
with col2:
    st.button("這是col2", key="4")
    st.button("這是col2", key="5")
    st.button("這是col2", key="6")
ans = 1
if "ans" not in st.session_state:
    st.session_state.ans = 1
if st.button("press add 1", key="ans2"):
    st.session_state.ans = st.session_state.ans + 1
st.write(f"ans={st.session_state.ans}")
image_folder = "images"
image_files = os.listdir(image_folder)
st.write(image_files)
st.title("圖片")
st.image("images/apple.png", width=300)
fruit = st.selectbox(
    "選擇水果",
    [
        "apple",
        "orange",
        "bananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananananan",
    ],
)
st.write(f"u choose {fruit}")
