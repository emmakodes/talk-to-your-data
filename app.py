import time
import streamlit as st
from chat_workflow import chain_workflow

# Custom image for the app icon and the assistant's avatar
assistant_logo = 'https://cdn.pixabay.com/photo/2016/06/28/13/51/dog-1484728_1280.png'

# Configure Streamlit page
st.set_page_config(
    page_title="Animals in Research",
    page_icon=assistant_logo
)

openai_api_key = st.sidebar.text_input('Input your OpenAI API Key', value="sk-", type = 'password')


# Initialize chat history
if 'messages' not in st.session_state:
    # Start with first message from assistant
    st.session_state['messages'] = [{"role": "assistant", 
                                  "content": "Hi user! ask me questions about animals in research"}]

for message in st.session_state.messages:
    if message["role"] == 'assistant':
        with st.chat_message(message["role"], avatar=assistant_logo):
            st.markdown(message["content"])
    else:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat logic
if query := st.chat_input("Ask me about animals in research"):
    if len(openai_api_key) <= 3:
        st.sidebar.error("☝️ Put in your openapi key")
    else:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": query})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(query)

        with st.chat_message("assistant", avatar=assistant_logo):
            message_placeholder = st.empty()
            # Send user's question to our chain

            # Initialize LLM chain
            chain = chain_workflow(openai_api_key=openai_api_key)
            result = chain({"question": query})
            response = result['answer']
            full_response = ""

            # Simulate stream of response with milliseconds delay
            for chunk in response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)

        # Add assistant message to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})