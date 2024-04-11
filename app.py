import streamlit as st
from src.utils import setup_dbqa

# Replacing deprecated caching method
@st.cache_resource
def get_dbqa():
    return setup_dbqa()

def main():
    st.title("[Test] Query NVIDIA's 2023 Financials")
    query = st.text_input("Enter your query:", "What was NVIDIA's total revenue in 2023?")
    if st.button("Submit"):
        try:
            dbqa = get_dbqa()
            response = dbqa({'query': query})
            answer = response.get("result", "No result found.")
            st.write(f"Answer: {answer}")
        except RuntimeError as e:
            st.error(f"Error loading the model: {e}")

if __name__ == "__main__":
    main()
