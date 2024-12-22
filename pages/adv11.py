import streamlit as st
from utils import init_page

init_page()
st.title("案一下以新增標題")
st.write("寫東西")
st.text("only word")
st.markdown(
    """
# only markdown
* **big bold**
* *shey text/*          
*italic*
* [link](https://www.google.com)

```python
print("hello world")
```      
"""
)
d = {"a": 1, "b": 2}
st.markdown(d)
st.write(d)
with st.expander("展開框"):
    st.write("被你發現了")
st.write("喜勒考喔我在外面")

st.write("---")
st.write('#number_input "輸入數字"')
number_input = st.number_input("輸入數字", min_value=0, max_value=100, value=50, step=5)
st.write(f"你輸入的數字是{number_input}")

st.write("---")
st.write("text_input 輸入文字")
text_input = st.text_input("輸入文字", placeholder="請輸入文字")
st.write(f"你輸入的文字是{text_input}")

st.write("---")
st.write("st.button 按鈕")
button = st.button("按鈕", key="btn1")
if button:
    st.write("你按下了按鈕")
    st.balloons()

st.write("---")
st.write("st.button 按鈕")
col1, col2 = st.columns(2)
if col1.button("按鈕", key="btn2"):
    st.write("你按下了按鈕")
    st.balloons()
if col2.button("按鈕", key="btn3"):
    st.write("你按下了按鈕")
    st.balloons()

col1, col2 = st.columns([1, 2])
col1.button("按鈕", key="btn4")
col2.button("按鈕", key="btn5")

col1, col2, col3 = st.columns([1, 2, 3])
col1.button("按鈕", key="btn6")
col2.button("按鈕", key="btn7")
col3.button("按鈕", key="btn8")
