import streamlit as st
from src.utils import setup_dbqa
import timeit

def main():
    st.title("Analyzing 10-K Filings submitted in 2023 for FAANG Companies: A Retrieval Augmented Generation (RAG) Approach")

    # Sidebar content with explanations for first-time users
    st.sidebar.header('About the App')
    st.sidebar.write("""
    **Overview:**
    This application uses a Retrieval Augmented Generation (RAG) approach, powered by OpenAI's "gpt-3.5-turbo-instruct",
    to analyze the latest 10-K filings (i.e 2023 Annual Financial Report) from FAANG companies. It provides insights into financial metrics and business performance.

    **Why Use RAG?**
    - **Data Privacy and Customization:** RAG allows organizations to analyze proprietary information securely within their own systems, reducing the risk of exposing sensitive data.
    - **Up-to-Date Insights:** Unlike GPT models which may not be trained on the most recent data, RAG utilizes the latest documents directly. For example, if analyzing Q4 results of a FAANG company released in early 2024, RAG would use this fresh information directly from the source, whereas GPT models would rely on data only up to their last training cut-off.
    - **Compliance with Data Residency Laws:** Ensures that data handling complies with local regulations by processing data within required jurisdictions.

    **Getting Started:**
    1. **Input Your Query:** Use the input box to type your financial query.
    2. **Submit Your Query:** Click 'Analyze Query' to see results.
    3. **View Results:** Read the insights and source documents provided.

    **Note on Query Length:**
    - The model can handle up to 4097 tokens. Keep queries concise to avoid errors.

    **Feedback and Contributions:**
    - Feedback is invaluable. Report issues and contribute via GitHub @ngweimeng.
    """)

    # User input for custom query
    user_query = st.text_input("Enter your query:", 
                               placeholder="E.g., Which FAANG company generated the highest revenue?")

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


