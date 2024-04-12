'''
===========================================
        Module: Open-source LLM Setup
===========================================
'''
from langchain.llms import OpenAI
import streamlit as st

def build_llm():
    llm = OpenAI(model="gpt-3.5-turbo-1106", temperature=0, openai_api_key=st.secrets["openai_api_key"])
    return llm



