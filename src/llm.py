'''
===========================================
        Module: Open-source LLM Setup
===========================================
'''
import os
from langchain.llms import OpenAI
import streamlit as st

def build_llm():
    llm = OpenAI(temperature=0, openai_api_key=st.secrets["openai_api_key"])
    return llm


