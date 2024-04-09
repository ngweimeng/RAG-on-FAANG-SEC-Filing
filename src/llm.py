'''
===========================================
        Module: Open-source LLM Setup
===========================================
'''
from langchain.llms import CTransformers

def build_llm():
    # Local CTransformers model
    llm = CTransformers(model="TheBloke/Llama-2-7b-Chat-GGML",
                        model_file="llama-2-7b-chat.ggmlv3.q8_0.bin",
                        config={'max_new_tokens': 256,
                                'temperature': 0.01}
                        )

    return llm