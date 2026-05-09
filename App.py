import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Rishi ChatBot", page_icon="🤖")

genai.configure(api_key=st.secrets["api_key"])
model=genai.GenerativeModel("models/gemini-2.5-flash")

st.title("Rishi ChatBot 🤖")
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Type your message here...")

if prompt:
    st.session_state.messages.append({"role": "user", 
                                      "content": prompt}
                                      )
    with st.chat_message("user"):
        st.write(prompt)

    response = model.generate_content(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
    with st.chat_message("assistant"):
        st.write(response.text)