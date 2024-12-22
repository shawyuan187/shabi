import streamlit as st
from utils import init_page

init_page()
st.title("聊天室")
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if message := st.chat_input("Enter chat"):
    with st.chat_message("user"):
        st.write(message)
    st.session_state.messages.append({"role": "user", "content": message})

    with st.chat_message("assistant"):
        st.write(f"這是示範回復:我收到你的訊息{message}")
    st.session_state.messages.append(
        {"role": "assistant", "content": f"這是示範回復:我收到你的訊息->{message}"}
    )
