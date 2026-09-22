from src.document_loader import load_documents
from src.text_splitter import split_documents
from src.vector_store import create_vector_store

documents = load_documents("data/documents")

chunks = split_documents(documents)

vector_store = create_vector_store(chunks)

results = vector_store.similarity_search(
    "How many paid leaves do employees get?",
    k=1
)

print("Search results:")

for result in results:
    print("\nContent:")
    print(result.page_content)

    print("\nMetadata:")
    print(result.metadata)