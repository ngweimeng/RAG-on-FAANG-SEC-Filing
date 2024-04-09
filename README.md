# RAG on NVIDEA's 2023 Annual Report

## Background

Access to Large Language Models (LLMs) such as OpenAI's GPT-4 has been revolutionized through user-friendly APIs, yet the need for self-hosted solutions persists due to strict data privacy and residency requirements. The rise of open-source LLMs offers an alternative to third-party providers, granting more control over model deployment.

Hosting LLMs in-house or on cloud services introduces compute capacity challenges. GPUs, while powerful, incur high costs. This project explores running quantized open-source LLMs on CPUs for document Q&A tasks using Retrieval Augmented Generation (RAG). The file we will run the document Q&A on is the  **96-page 2023 annual report of NVIDEA**

## Quantization Overview

Large Language Models (LLMs) are powerful yet typically require significant compute and memory resources. Quantization addresses this by compressing the models, thereby shrinking their memory usage and speeding up inference without markedly sacrificing performance.

In essence, quantization lowers the bit representation of numbers—in this case, the model's weights. By converting, for example, 16-bit floating-point weights to 8-bit integers, we significantly reduce the model size. This process makes LLMs viable for deployment on CPUs and embedded systems with limited resources.

## Tools and Libraries

- **LangChain**: A framework to build applications that leverage language model capabilities.
- **C Transformers**: Provides Python bindings for highly efficient Transformer models using the GGML library, optimized for C/C++.
- **FAISS**: A library for fast similarity search and clustering of dense vectors, aiding in the efficient handling of large datasets.
- **Sentence-Transformers (all-MiniLM-L6-v2)**: A pre-trained transformer model generating 384-dimensional vectors from text, enhancing semantic search and clustering applications.
- **Llama-2-7B-Chat**: A dialogue-centric Llama 2 model fine-tuned with extensive instruction datasets and over a million human annotations for conversational AI.

## Implementation Guide

### Step 1: Data Processing & Vector Store Creation
- Ingest data, split into manageable chunks.
- Load the Sentence-Transformers model for embedding generation.
- Index and save chunks in the FAISS vector store at 'vectorstore/db_faiss'.

### Step 2: Prompt Template Setup
- Use appropriate prompt templates for the Llama-2-7B-Chat model, avoiding conversational formats not optimized for this model.

### Step 3: Download Llama-2-7B-Chat Model
- Download the quantized Llama-2-7B-Chat model GGML binary from Hugging Face.

### Step 4: LLM Setup
- Use the CTransformers LLM wrapper from LangChain to integrate the downloaded GGML model.

### Step 5: RetrievalQA Initialization
- Implement functions to create a LangChain RetrievalQA object for document Q&A capabilities.

### Step 6: Main Script Assembly
- Use `argparse` for CLI input and integrate all components into `app.py`.

### Step 7: Streamlit Deployment
```bash
streamlit run app.py
```


