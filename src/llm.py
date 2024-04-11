'''
===========================================
        Module: Open-source LLM Setup
===========================================
'''
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/roberta-base-squad2"

def build_llm():
    # Local CTransformers model
    llm = AutoModelForQuestionAnswering.from_pretrained(model_name)

    return llm
