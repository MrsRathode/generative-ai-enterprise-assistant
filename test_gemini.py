from langchain_google_genai import ChatGoogleGenerativeAI
from src.config import GOOGLE_API_KEY

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY
)

response = model.invoke("Explain what an AI assistant is in one simple sentence.")

print(response.content)