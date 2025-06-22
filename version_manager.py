import chromadb
from chromadb.utils import embedding_functions

client = chromadb.HttpClient(host="localhost", port=8000)  # Use Chroma Server mode

collection = client.get_or_create_collection(
    name="book_versions",
    embedding_function=embedding_functions.DefaultEmbeddingFunction()
)

def save_version(content, tag):
    collection.add(documents=[content], ids=[tag])

    with open(f"{tag}.md", "w", encoding="utf-8") as f:
        f.write(content)

    with open("chapter1.md", "a", encoding="utf-8") as f:
        f.write(f"\n\n---\n## {tag}\n\n")
        f.write(content)

def search_version(query):
    result = collection.query(query_texts=[query], n_results=1)
    docs = result.get("documents", [])
    if docs and docs[0]:
        return docs[0][0]
    return "No result found."

def list_versions():
    return collection.get()["ids"]
