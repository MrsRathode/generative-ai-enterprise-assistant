import streamlit as st

from src.document_loader import load_documents
from src.text_splitter import split_documents
from src.vector_store import create_vector_store
from src.rag_chain import create_rag_chain


st.set_page_config(
    page_title="Generative AI Enterprise Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Generative AI Enterprise Assistant")
st.write("Ask questions about the company HR policy.")


@st.cache_resource
def initialize_system():
    documents = load_documents("data/documents")
    chunks = split_documents(documents)
    vector_store = create_vector_store(chunks)
    ask_question = create_rag_chain(vector_store)

    return vector_store, ask_question


vector_store, ask_question = initialize_system()


question = st.text_input("Enter your question:")


if question:

    with st.spinner("Searching documents and generating answer..."):

        results = vector_store.similarity_search(
            question,
            k=2
        )

        answer = ask_question(question)

    st.subheader("🤖 Answer")
    st.write(answer)

    st.subheader("📄 Source")

    source_files = set(
        result.metadata.get("filename", "Unknown")
        for result in results
    )

    for filename in source_files:
        st.write(f"**Document:** {filename}")

    with st.expander("🔎 View Retrieved Information"):

        for i, result in enumerate(results):

            st.markdown(f"**Retrieved Chunk {i + 1}**")

            st.write(result.page_content)