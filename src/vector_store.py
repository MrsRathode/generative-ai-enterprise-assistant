from langchain_community.vectorstores import FAISS
from src.embeddings import create_embeddings


def create_vector_store(chunks):
    embeddings = create_embeddings()

    texts = [chunk["content"] for chunk in chunks]
    metadatas = [
        {"filename": chunk["filename"]}
        for chunk in chunks
    ]

    vector_store = FAISS.from_texts(
        texts=texts,
        embedding=embeddings,
        metadatas=metadatas
    )

    return vector_store