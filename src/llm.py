'''
===========================================
        Module: Open-source LLM Setup
===========================================
'''
import os
from langchain.llms import OpenAI

def build_llm():
    #openai_api_key = os.getenv('OPENAI_API_KEY')
    #if openai_api_key is None:
    #    raise ValueError("No OpenAI API key found in environment variables")
    llm = OpenAI(temperature=0, openai_api_key=open_api_key)
    return llm

