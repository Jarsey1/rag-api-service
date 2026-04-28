import os
from fastapi import FastAPI
from qdrant_client import QdrantClient

app = FastAPI()

# This uses the environment variable we defined in your docker-compose.yml
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")

@app.get("/health")
def health_check():
    try:
        client = QdrantClient(url=QDRANT_URL)
        # Attempt to get collections to verify connectivity
        collections = client.get_collections()
        return {"status": "connected", "collections": collections.collections}
    except Exception as e:
        return {"status": "error", "message": str(e)}