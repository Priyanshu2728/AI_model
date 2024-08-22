import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyCoUBngFQJOQ-FriGJm4O0kTsAS8Ki5tGA")


model = genai.GenerativeModel('gemini-1.0-pro-latest')
chat = model.start_chat(history=[])


st.title("Hey! Give your thought..")


text = st.text_input("Enter your message:")

if st.button("Send"):
    response = chat.send_message(text)
    st.write("Model's response:")
    st.write(response.text)
