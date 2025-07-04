# server.py
import streamlit as st
from app import get_response

st.set_page_config(page_title="AI Content Editor", layout="centered")

st.title("AI Content Editor Bot")
st.write(
    "Give me some text, and I will:\n"
    "-  Correct grammar\n"
    "-  Expand it\n"
    "- 🏷 Add hashtags\n"
)

user_input = st.text_area("Enter your text here:", height=150)

task = st.selectbox(
    "Select a task:",
    ("all", "grammar", "expand", "hashtags"),
    index=0
)

if st.button("Generate"):
    if user_input.strip():
        with st.spinner("Thinking..."):
            response = get_response(user_input, task)
            st.markdown("###  Output:")
            st.write(response)
    else:
        st.warning("Please enter some text.")
