import logging
from src.utils import setup_dbqa

logging.basicConfig(level=logging.DEBUG)

@st.cache_resource
def get_dbqa():
    try:
        return setup_dbqa()
    except Exception as e:
        logging.error("Failed to initialize the DBQA system: %s", str(e))
        raise

def retrieve_answers(query):
    try:
        dbqa = get_dbqa()  # Retrieve the cached DBQA object
        start = timeit.default_timer()
        response = dbqa({'query': query})
        end = timeit.default_timer()
        time_elapsed = end - start
        answer = response["result"]
        source_docs = response['source_documents']
        sources = []

        for doc in source_docs:
            sources.append({
                "text": doc.page_content,
                "source": doc.metadata["source"],
                "page": doc.metadata["page"]
            })
        return answer, sources, time_elapsed
    except Exception as e:
        logging.error("Error during query retrieval: %s", str(e))
        raise

# Streamlit main function with error handling
def main():
    st.title("[Test2] NVIDIA's 2023 Financial Report Insights")

    query = st.text_input("Enter your query, e.g., 'What was NVIDIA's total revenue in 2023?'")
    if st.button("Ask Query"):
        try:
            answer, sources, time_elapsed = retrieve_answers(query)
            st.success(answer)
            st.write(f"Time to retrieve response: {time_elapsed:.2f} seconds")
            for i, source in enumerate(sources):
                st.write(f"Source Document {i+1}: {source['source']} (Page {source['page']})")
                st.text_area("Content", source['text'], height=150)
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
