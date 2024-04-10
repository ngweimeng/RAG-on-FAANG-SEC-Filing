import streamlit as st
from src.utils import setup_dbqa

def retrieve_answers(query):
    dbqa = setup_dbqa()
    response = dbqa({'query': query})
    
    answer = response["result"]
    source_docs = response['source_documents']
    sources = []

    for i, doc in enumerate(source_docs):
        source_info = {
            "text": doc.page_content,
            "source": doc.metadata["source"],
            "page": doc.metadata["page"]
        }
        sources.append(source_info)
    
    return answer, sources

def main():
    st.title("Retrieval-Augmented Generation (RAG) on NVIDIA's 2023 Annual Financial Report")

    text_input = st.text_area("Write your Query below: i.e What was NVIDIA's total revenue in 2023?\n 
    What were NVIDIA's key social responsibility initiatives in 2023?\n 
    How did NVIDIA's market share in graphics and compute sectors evolve in 2023?\n")

    if st.button("Ask Query"):
        if len(text_input) > 0:
            st.info("Your Query: " + text_input)
            try:
                answer, sources = retrieve_answers(text_input)
                st.success(answer)
                
                for i, source in enumerate(sources):
                    st.write(f"Source Document {i+1}")
                    st.text(f"Source Text: {source['text']}")
                    st.text(f"Document Name: {source['source']}")
                    st.text(f"Page Number: {source['page']}")
                    st.write("="*60)
                    
            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
