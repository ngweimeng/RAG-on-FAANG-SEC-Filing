'''
===========================================
        Module: Open-source LLM Setup
===========================================
'''
from langchain_community.llms import CTransformers
import logging

logging.basicConfig(level=logging.INFO)

def build_llm():
    try:
        # Specify the model details explicitly
        model_name = 'TheBloke/Llama-2-7B-Chat-GGUF'
        model_file = 'llama-2-7b-chat.Q4_K_M.gguf'
        logging.info(f"Attempting to load model {model_name} from file {model_file}")
        llm = CTransformers(model=model_name, model_file=model_file)
        return llm
    except Exception as e:
        logging.error(f"Failed to load model {model_name}. Error: {e}")
        raise

