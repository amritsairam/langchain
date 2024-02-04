import streamlit as st
from dotenv import load_dotenv
load_dotenv()  # Ensure this line is executed correctly

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, AIMessage, HumanMessage

# st.title('Q&A chatbot')
llm = ChatOpenAI()

if 'key' not in st.session_state:
    st.session_state['flow'] = [SystemMessage(content="you are a comedian ai assistant")]



def qa_chatbot(input):
        st.session_state['flow'].append(HumanMessage(content=input))
        response = llm(st.session_state['flow'])  # Pass the string input
        st.session_state['flow'].append(AIMessage(content=response.content))
        return response.content

input=st.text_input("Input: ",key="input")
response=qa_chatbot(input)

submit=st.button("Ask the question")

if submit:
    st.subheader("The Response is")
    st.write(response)



