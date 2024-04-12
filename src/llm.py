'''
===========================================
        Module: Open-source LLM Setup
===========================================
'''
import os
from langchain.llms import OpenAI

def build_llm():
    llm = OpenAI(temperature=0, openai_api_key=openai_api_key)
    return llm

