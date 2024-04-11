import streamlit as st
from src.utils import setup_dbqa
import timeit

# Initialize DBQA only once when the Streamlit app starts
@st.cache_resource
def get_dbqa():
    return setup_dbqa()

def retrieve_answers(query):
    dbqa = get_dbqa()  # Retrieve the cached DBQA object

    start = timeit.default_timer()  # Start timing
    response = dbqa({'query': query})
    end = timeit.default_timer()  # End timing

    time_elapsed = end - start  # Calculate the time elapsed

    answer = response["result"]
    source_docs = response['source_documents']
    sources = []

    for doc in source_docs:
        source_info = {
            "text": doc.page_content,
            "source": doc.metadata["source"],
            "page": doc.metadata["page"]
        }
        sources.append(source_info)

    return answer, sources, time_elapsed

def main():
    st.title("Retrieval-Augmented Generation (RAG) on NVIDIA's 2023 Annual Financial Report")

    text_input = st.text_input("Write your Query below: i.e., 'What was NVIDIA's total revenue in 2023?'")
                            
    if st.button("Ask Query"):
        if len(text_input) > 0:
            st.info("Your Query: " + text_input)
            try:
                answer, sources, time_elapsed = retrieve_answers(text_input)
                st.success(answer)
                
                st.write(f"Time to retrieve response: {time_elapsed:.2f} seconds")  # Display time taken
                st.write("="*60)

                for i, source in enumerate(sources):
                    st.subheader(f"Source Document {i+1}")
                    st.text(f"Source Text: {source['text']}")
                    st.text(f"Document Name: {source['source']}")
                    st.text(f"Page Number: {source['page']}")
                    st.write("="*60)
                    
            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

