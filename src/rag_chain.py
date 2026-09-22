from langchain_google_genai import ChatGoogleGenerativeAI
from src.config import GOOGLE_API_KEY


def create_rag_chain(vector_store):
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GOOGLE_API_KEY,
        temperature=0
    )

    def ask_question(question):
        results = vector_store.similarity_search(question, k=2)

        context = "\n\n".join(
            result.page_content for result in results
        )

        prompt = f"""
You are an enterprise AI assistant.

Answer the user's question using only the provided context.

If the answer is not available in the context, say:
"I could not find that information in the provided documents."

Context:
{context}

Question:
{question}

Answer:
"""

        response = model.invoke(prompt)

        return response.content

    return ask_question