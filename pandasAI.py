# import os
# import openai
# import sys
# sys.path.append('../..')
# from dotenv import load_dotenv, find_dotenv
# _ = load_dotenv(find_dotenv()) # read local .env file

import streamlit as st 
import pandas as pd 
import numpy as np  
from pandasai.llm import  OpenAI
from pandasai import SmartDataframe
from pandasai.helpers.openai_info import get_openai_callback
import yfinance as yf
api_key  = st.secrets['OPENAI_API_KEY'] 


st.title('Chat with a Stock')

fileNm = st.file_uploader('Upload your own data: ')
if fileNm:
    uploaded_df = pd.read_csv(fileNm)
    st.dataframe(uploaded_df)

fileNm2 = st.file_uploader('Upload some of your own data: ')

# ticker = st.text_input('Symbol', '^NDX')
ticker = st.text_input('Enter Symbol', 'INTC')

llm = OpenAI(api_token=api_key)
dfdaily = yf.download(ticker, period="1mo", interval = "1d")

df = SmartDataframe(dfdaily, config={"llm": llm, "conversational": True})

def generate_chart(input_table):
    st.line_chart(input_table['Adj Close'])

with st.expander("See data"):
    st.dataframe(dfdaily)
    generate_chart(dfdaily)

def generate_response(input_text):
#    llm = OpenAI(temperature=0.7, openai_api_key=open_api_key)
    with get_openai_callback() as cb:
        response = df.chat(input_text)

    st.info(response)
    # print(response)

# def get_logo(input_symbol):


with st.form('my_form'):
   text = st.text_area('Ask your question:', 'What was the price on 2024-01-01?')
   if submitted := st.form_submit_button('Submit'):
   # if not open_api_key.startswith('sk-'):
   #    st.warning('Please enter your OpenAI API Key!')
   # if submitted and open_api_key.startswith('sk-'):
      generate_response(text) 



st.caption("Copyright @ Madhu Ram 2023")