def run_workflow(question, vector_store, ask_question):
    # Step 1: Retrieve relevant documents
    results = vector_store.similarity_search(question, k=2)

    # Step 2: Generate an answer using the retrieved information
    answer = ask_question(question)

    # Step 3: Return both the retrieved information and answer
    return {
        "question": question,
        "retrieved_documents": results,
        "answer": answer
    }