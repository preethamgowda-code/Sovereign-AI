import chromadb
from chromadb.config import Settings

class SovereignMemory:
    def __init__(self):
        # Persistent storage ensures memory survives a reboot
        self.client = chromadb.PersistentClient(path="./data/chroma_db")
        self.collection = self.client.get_or_create_collection(
            name="audit_memory",
            metadata={"hnsw:space": "cosine"} # 2026 standard for semantic similarity
        )

    def store_insight(self, insight_text, metadata):
        # Vectorize and store the enterprise breakthrough
        self.collection.add(
            documents=[insight_text],
            metadatas=[metadata],
            ids=[f"id_{metadata['timestamp']}"]
        )