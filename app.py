import streamlit as st
from src.utils import setup_dbqa
import timeit

def main():
    st.title("Analyzing 10-K Filings Submitted in 2023 for FAANG Companies: A Retrieval Augmented Generation (RAG) Approach")

    # User input for custom query
    user_query = st.text_input("Enter your query:", 
                               placeholder="E.g., What is the breakdown of Amazon's Operating Income?")

    # Button to trigger the computation
    if st.button('Analyze Query'):
        if user_query:  # Ensure there is a query to process
            with st.spinner('Fetching data...'):
                start = timeit.default_timer()
                dbqa = setup_dbqa()
                response = dbqa({'query': user_query})
                end = timeit.default_timer()

                time_elapsed = end - start

                if response["result"]:
                    st.success(f'Answer: {response["result"]}')
                else:
                    st.error("No answer found.")

                # Process source documents
                if 'source_documents' in response:
                    st.write('### Source Documents')
                    for i, doc in enumerate(response['source_documents']):
                        st.write(f'#### Source Document {i+1}')
                        st.text(f'Source Text: {doc.page_content}')
                        st.text(f'Document Name: {doc.metadata["source"]}')
                        st.text(f'Page Number: {doc.metadata["page"]}')
                        st.write('='*60)
                st.info(f"Time to retrieve response: {time_elapsed:.2f} seconds")
        else:
            st.warning("Please enter a query to analyze.")

if __name__ == '__main__':
    main()
