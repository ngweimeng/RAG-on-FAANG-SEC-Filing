'''
===========================================
        Module: Prompts collection
===========================================
'''

qa_template = """Use the following pieces of information to answer the user's question.
If you don't know the answer, say that you do not know. Do not make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""
