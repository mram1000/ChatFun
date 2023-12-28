# from openai import OpenAI
import streamlit as st 
import pandas as pd 
import numpy as np 
from langchain.llms import OpenAI 


st.title("Chat GPT Fun")

# Retrieve Open AI key
open_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(input_text):
   llm = OpenAI(temperature=0.7, openai_api_key=open_api_key)
   st.info(llm(input_text))

with st.form('my_form'):
   text = st.text_area('Enter text:', 'Write a 1 stanza poem about the beauty of rain')
   submitted = st.form_submit_button('Submit')
   if not open_api_key.startswith('sk-'):
      st.warning('Please enter your OpenAI API Key!')
   if submitted and open_api_key.startswith('sk-'):
      generate_response(text) 
  

# set default model in session state
# if "openai_model" not in st.session_state:
#    st.session_state["openai_model"] = "gpt-3.5-turbo"

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])


# Accept user input
# if prompt := st.chat_input("Say something"):

#   with st.chat_message("user"):
#     st.markdown(prompt)

#   # add prompt to state history
#   st.session_state.messages.append({"role": "user", "content": prompt})


#   with st.chat_message("assistant"):  
#     message_placeholder = st.empty()
#     full_response = ""
    
#   for response in client.chat.completions.create(
#      model = st.session_state["openai_model"],
#      messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
#      stream=True,
#     ):
#     full_response += (response.choices[0].delta.content or "")
#     message_placeholder.markdown(full_response + "|")
  
#   message_placeholder.markdown(full_response)

#   st.session_state.messages.append({"role": "assistant", "content": full_response})




