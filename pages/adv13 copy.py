import streamlit as st
from utils import init_page

init_page()
st.title("聊天室示範")
demo_messages = [
    {"role": "user", "content": "你好，請問怎麼學python?"},
    {
        "role": "assistant",
        "content": "學習python的基本步驟:\n1.了解基礎與法\2.練習寫簡單城市\n3.解決實際問題",
    },
    {"role": "user", "content": "看起來不難ㄟ"},
    {"role": "assistant", "content": "yesssss事是幾個簡單城市"},
]
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
    if message := st.chat_input("inter chat"):
        with st.chat_message("user"):
            st.write(message)
    assistant_response = f"u say:{message}"
    with st.chat_message("assistant"):
        st.write(assistant_response)
        st.session_state.messages.append(
            {"role": "assistant", "content": assistant_response}
        )
