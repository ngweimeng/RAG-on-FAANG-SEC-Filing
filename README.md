# Analyzing 10-K Filings submitted in 2023 for FAANG Companies: A Retrieval Augmented Generation (RAG) Approach

This project leverages a Retrieval Augmented Generation (RAG) approach to analyze the 2023 10-K filings of FAANG companies. It provides insights into financial metrics and business performance directly from financial documents.

## Background

This project aims to simplify the process of extracting specific financial information from the dense and extensive 10-K filings of FAANG companies. Using advanced NLP techniques and machine learning, it answers queries related to financial data by retrieving relevant information from the filings and generating concise answers.

## Why RAG?

Retrieval Augmented Generation (RAG) combines the best of both retrieval-based and generative NLP approaches. By retrieving pertinent information and then generating text based on that information, RAG provides highly accurate and contextually relevant answers. This approach is particularly beneficial for organizations that handle sensitive or proprietary information for several reasons:

- **Data Privacy and Security**: With RAG, it is possible to deploy models within a secure, private environment, ensuring that sensitive data never leaves the organizational boundaries.
- **Compliance with Data Residency Laws**: RAG can be deployed on local servers or private clouds to meet specific jurisdictional data residency requirements, an essential factor for many industries such as finance and healthcare.
- **Customization for Proprietary Needs**: RAG allows organizations to customize both the retrieval and generation phases, using proprietary data sets that offer competitive advantages without exposing them externally.
  
## Tools/Libraries

- **Streamlit**: For creating the web interface.
- **Langchain**: Used for setting up the RetrievalQA framework and handling document embeddings.
- **FAISS**: For efficient similarity search and information retrieval from high-dimensional data.
- **Hugging Face Transformers**: Provides pre-trained models used for generating embeddings and textual responses.
- **OpenAI "gpt-3.5-turbo-instruct"**: Utilized for generating responses based on the retrieved information, known for its ability to understand and generate informative, concise, and accurate answers.

## Using the Application

Access the Streamlit application directly via:

[FAANG 2023 Annual Report Analysis App](https://faang-2023-annual-report.streamlit.app/)

### How to Use

- Navigate to the provided URL to access the web application.
- Enter your query related to the financial data of FAANG companies in the input box.
- Press the "Analyze Query" button to process your query.
- View the answer and the source documents that were used to generate the response.

### Note on Usage

The application's underlying model, OpenAI's "gpt-3.5-turbo-instruct", supports a maximum context length of 4097 tokens. Occasionally, if your query combined with the necessary contextual data exceeds this limit, the model will not be able to process the request and will return an error. 

To ensure your queries are processed successfully:
- **Keep Your Queries Concise**: Try to formulate your questions as succinctly as possible.
- **Split Complex Queries**: If your query is naturally long or complex, consider breaking it into smaller, separate questions.
- **Monitor Token Usage**: Be aware of the length of both your queries and the expected completion. Reduce unnecessary details in your questions.

These adjustments will help avoid surpassing the token limit and ensure a smoother experience using the application.

## Conclusion

This tool is designed to assist financial analysts, investors, and enthusiasts in quickly obtaining clear and concise answers from complex financial documents, enhancing understanding and decision-making processes.

For feedback, issues, or contributions, feel free to interact through the Streamlit app's feedback system or directly via GitHub issues.



