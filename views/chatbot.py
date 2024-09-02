import random
import time

import streamlit as st


# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello migo/miga!",
            "How can I help you today?",
            "Nganong gwapa man ko?",
            "It's a prank!! Wa man jud koy klaro ka storya",
            "Nganong naa pa man ka diri?",
            "Wa ko kabalo.. maypa pag exit na HAHAHAHAHAHA"
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Type something and see a miracle"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
