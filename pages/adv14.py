import streamlit as st
import openai
import os
from dotenv import load_dotenv
from utils import init_page

init_page()
# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize Streamlit page
st.title("聊天室")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from session state
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Input from user
if message := st.chat_input("Enter chat"):
    # Add user message to chat
    with st.chat_message("user"):
        st.write(message)
    st.session_state.messages.append({"role": "user", "content": message})

    # Get assistant response
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "你是一位專業的小幫手，幫助人們解決困難"},
                {"role": "user", "content": message},
            ]
            + st.session_state.messages,
            max_tokens=100,
            temperature=0.7,
        )
        # Extract assistant's content
        assistant_content = response["choices"][0]["message"]["content"]
        with st.chat_message("assistant"):
            st.write(assistant_content)
        # Add assistant's response to session state
        st.session_state.messages.append(
            {"role": "assistant", "content": assistant_content}
        )
    except openai.error.OpenAIError as e:
        st.error(f"OpenAI API Error: {e}")
    except Exception as e:
        st.error(f"Unexpected Error: {e}")
