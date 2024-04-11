import streamlit as st
from src.utils import setup_dbqa
import timeit

def main():
    st.title("NVIDIA 2023 Revenue Query")
    
    # Button to trigger the computation
    if st.button('Get NVIDIA\'s Total Revenue in 2023'):
        with st.spinner('Fetching data...'):
            start = timeit.default_timer()
            dbqa = setup_dbqa()
            response = dbqa({'query': "What was NVIDIA's total revenue in 2023?"})
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

if __name__ == '__main__':
    main()
