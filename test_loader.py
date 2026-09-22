from src.document_loader import load_documents

documents = load_documents("data/documents")

for document in documents:
    print("File:", document["filename"])
    print(document["content"])