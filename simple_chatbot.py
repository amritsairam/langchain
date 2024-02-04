from langchain.llms.openai import OpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()  # Load API key from .env file

st.title('Q&A Chatbot')

input = st.text_input('Input:', key='input')
submit = st.button('Ask the question')

def getopenairesponse(input):
    llm = OpenAI(model='gpt-3.5-turbo-instruct', temperature=0.6)
    response = llm(input)
    return response

if submit:
    response = getopenairesponse(input)  # Call the function after button click
    st.subheader('The response is:')
    st.write(response)  # Display the returned response

# def getopenairesponse(input):
#     llm = OpenAI(model='gpt-3.5-turbo-instruct', temperature=0.6)
#     response = llm(input)
#     return response 