'''
===========================================
        Module: Open-source LLM Setup
===========================================
'''
from langchain.llms import OpenAI
import streamlit as st

def build_llm():
    llm = OpenAI(model="gpt-3.5-turbo-0125", openai_api_key=st.secrets["openai_api_key"])
    
    def complete(prompt):
        response = llm.chat_completions(messages=[{"role": "system", "content": "You are a helpful assistant."},
                                                  {"role": "user", "content": prompt}])
        return response['choices'][0]['message']['content']

    return complete




