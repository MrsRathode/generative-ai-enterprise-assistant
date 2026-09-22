from src.document_loader import load_documents
from src.text_splitter import split_documents
from src.vector_store import create_vector_store
from src.rag_chain import create_rag_chain


# 1. Load documents
documents = load_documents("data/documents")

# 2. Split documents into chunks
chunks = split_documents(documents)

# 3. Create FAISS vector store
vector_store = create_vector_store(chunks)

# 4. Create RAG chain
ask_question = create_rag_chain(vector_store)

# 5. Ask a question
question = "How many paid leaves do employees get?"

answer = ask_question(question)

print("\nQuestion:")
print(question)

print("\nAnswer:")
print(answer)