from src.document_loader import load_documents
from src.text_splitter import split_documents

documents = load_documents("data/documents")

chunks = split_documents(documents)

print("Total chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print("\nChunk", i + 1)
    print("File:", chunk["filename"])
    print("Content:", chunk["content"])