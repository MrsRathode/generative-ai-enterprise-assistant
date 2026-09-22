from src.document_loader import load_documents
from src.text_splitter import split_documents
from src.vector_store import create_vector_store
from src.rag_chain import create_rag_chain
from src.evaluator import evaluate_answer


# Load and process documents
documents = load_documents("data/documents")
chunks = split_documents(documents)

# Create vector store
vector_store = create_vector_store(chunks)

# Create RAG function
ask_question = create_rag_chain(vector_store)

# Ask question
question = "How many paid leaves do employees get?"

# Generate answer
answer = ask_question(question)

# Get relevant context
results = vector_store.similarity_search(question, k=2)

context = "\n\n".join(
    result.page_content for result in results
)

# Evaluate answer
evaluation = evaluate_answer(answer, context)

print("\nQuestion:")
print(question)

print("\nAnswer:")
print(answer)

print("\nEvaluation:")
print(evaluation["message"])