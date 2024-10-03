import streamlit as st
import asyncio
from bot import chatbot

st.title("Chatbot Application")

# Function to handle chat
async def handle_chat(user_input):
    response = await chatbot.generate_response(user_input)
    return response

# Streamlit chat interface
if 'messages' not in st.session_state:
    st.session_state.messages = []

st.text_input("You: ", key='user_input', on_change=lambda: st.session_state.messages.append({"role": "user", "content": st.session_state.user_input}))

if st.button("Send"):
    user_input = st.session_state.user_input
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        response = asyncio.run(handle_chat(user_input))
        st.session_state.messages.append({"role": "assistant", "content": response})

# Display messages
for message in st.session_state.messages:
    role = "You" if message['role'] == 'user' else "Assistant"
    st.markdown(f"**{role}:** {message['content']}")
