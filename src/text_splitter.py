from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = []

    for document in documents:
        text_chunks = splitter.split_text(document["content"])

        for chunk in text_chunks:
            chunks.append({
                "filename": document["filename"],
                "content": chunk
            })

    return chunks