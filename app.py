import streamlit as st
from src.utils import setup_dbqa

# Replacing deprecated caching method
@st.cache_resource
def get_dbqa():
    return setup_dbqa()

def main():
    st.title("Query NVIDIA's 2023 Financials")
    query = st.text_input("Enter your query:", "What was NVIDIA's total revenue in 2023?")

    if st.button("Submit"):
        with st.spinner('Fetching results...'):
            dbqa = get_dbqa()
            response = dbqa({'query': query})
            answer = response.get("result", "No result found.")
            st.write(f"Answer: {answer}")
            # Additional info
            st.write("Source documents:")
            for i, doc in enumerate(response.get('source_documents', [])):
                st.write(f"Document {i+1}: {doc.metadata['source']} (Page {doc.metadata['page']})")
                st.text_area("Content", doc.page_content, height=100)

if __name__ == "__main__":
    main()
