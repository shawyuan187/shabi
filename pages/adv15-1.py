import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
from utils import init_page

init_page()
# Load environment variables
load_dotenv()

# Set OpenAI API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize Streamlit page
st.title("搜尋問答 AI")

# Input from user
if message := st.chat_input("請輸入您想前往的頁面"):
    # Add user message to chat
    with st.chat_message("user"):
        st.write(message)

    # Get assistant response
    try:
        # Get list of pages
        pages_files_path = os.listdir("pages")
        pages_list = "\n".join(pages_files_path)

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": f"你是一位專業的小幫手，幫助人們找到他們想要的頁面。以下是可用的頁面列表：\n{pages_list}\n請根據使用者的輸入，回傳一個最相近的頁面名稱，格式為：'頁面名稱: <page_name>'，只能回傳一個頁面。",
                },
                {"role": "user", "content": message},
            ],
        )
        # Extract assistant's content
        assistant_content = response.choices[0].message.content
        with st.chat_message("assistant"):
            st.write(assistant_content)

        # Find the closest page match
        closest_match = None
        if "頁面名稱: " in assistant_content:
            closest_match = assistant_content.split("頁面名稱: ")[1].strip()

        if closest_match and closest_match in pages_files_path:
            st.link_button(f"前往 {closest_match}", f"{closest_match[:-3]}")
        else:
            st.write("找不到相符的頁面")

    except Exception as e:
        st.error(f"An error occurred: {e}")
        st.stop()
