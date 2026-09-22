from src.embeddings import create_embeddings

embeddings = create_embeddings()

result = embeddings.embed_query(
    "How many paid leaves do employees get?"
)

print("Embedding created successfully!")
print("Vector length:", len(result))
print("First 5 values:", result[:5])