'''
===========================================
        Module: Open-source LLM Setup
===========================================
'''
from langchain_community.llms import CTransformers

def build_llm():
    # Local CTransformers model

    llm = CTransformers(model='TheBloke/Llama-2-7B-Chat-GGUF', model_file='llama-2-7b-chat.Q4_K_M.gguf')    
    return llm

