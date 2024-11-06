from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

import logging
logging.basicConfig(level=logging.DEBUG)

# os.environ['OPEN_API_KEY']=os.getenv('OPEN_API_Key')
load_dotenv()
# Prompt Template


prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template("You are a helpful assistant. Please respond to user queries."),
        HumanMessagePromptTemplate.from_template("Question: {question}")
    ]
)

# streamlit framework

st.title('Langchain demo with LLAMA2 API')
input_text = st.text_input('Search the topic you want')

# openai llm

llm= Ollama(model='llama2')
output_parser=StrOutputParser()
chain = prompt|llm|output_parser

# Display response
if input_text:
    response = chain.invoke({'question': input_text})
    st.write(response)