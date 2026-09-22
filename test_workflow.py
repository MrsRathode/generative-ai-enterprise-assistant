from src.document_loader import load_documents
from src.text_splitter import split_documents
from src.vector_store import create_vector_store
from src.rag_chain import create_rag_chain
from src.workflow import run_workflow


# 1. Load documents
documents = load_documents("data/documents")

# 2. Split documents
chunks = split_documents(documents)

# 3. Create vector store
vector_store = create_vector_store(chunks)

# 4. Create RAG answer function
ask_question = create_rag_chain(vector_store)

# 5. Run the multi-step workflow
question = "How many paid leaves do employees get?"

result = run_workflow(
    question,
    vector_store,
    ask_question
)

print("\nQuestion:")
print(result["question"])

print("\nRetrieved Information:")
for document in result["retrieved_documents"]:
    print(document.page_content)

print("\nFinal Answer:")
print(result["answer"])