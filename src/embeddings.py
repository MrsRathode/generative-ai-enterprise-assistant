from langchain_google_genai import GoogleGenerativeAIEmbeddings
from src.config import GOOGLE_API_KEY


def create_embeddings():
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
        google_api_key=GOOGLE_API_KEY
    )

    return embeddings