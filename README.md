# 🤖 Generative AI Enterprise Assistant

An AI-powered enterprise assistant that uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from company documents and generate context-aware responses.

## 🚀 Live Demo

👉 [Open the Live Application](https://generative-ai-enterprise-assistant-edra8upsd4eupidkiiqgbr.streamlit.app/)

## 📌 Project Overview

The Generative AI Enterprise Assistant allows users to ask questions about enterprise documents.

The system retrieves relevant information from documents using semantic search and then uses Google's Gemini model to generate context-aware answers based only on the retrieved information.

If the required information is not available in the provided documents, the assistant clearly indicates that the information could not be found.

## ✨ Features

- 📄 Enterprise document loading
- ✂️ Text chunking
- 🔎 Semantic search using embeddings
- 🗂️ FAISS vector store
- 🤖 Google Gemini for answer generation
- 🔗 LangChain-based RAG workflow
- 📚 Context-aware responses
- 🛡️ Fallback for unavailable information
- 🌐 Streamlit web interface
- 🚀 Live deployment

## 🛠️ Tech Stack

- Python
- LangChain
- Google Gemini
- Google Generative AI Embeddings
- FAISS
- Streamlit
- Python-dotenv

## 🔄 How It Works

```text
User Question
      ↓
Document Loading
      ↓
Text Chunking
      ↓
Generate Embeddings
      ↓
FAISS Similarity Search
      ↓
Retrieve Relevant Context
      ↓
Gemini LLM
      ↓
Context-Aware Answer

📂 Project Structure

generative-ai-enterprise-assistant/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── data/
│   └── documents/
│       └── hr_policy.txt
│
├── src/
│   ├── config.py
│   ├── document_loader.py
│   ├── embeddings.py
│   ├── evaluator.py
│   ├── rag_chain.py
│   ├── text_splitter.py
│   ├── vector_store.py
│   └── workflow.py
│
├── test_embeddings.py
├── test_evaluator.py
├── test_gemini.py
├── test_loader.py
├── test_rag.py
├── test_splitter.py
├── test_vector_store.py
└── test_workflow.py

