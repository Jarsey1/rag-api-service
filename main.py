import os
from fastapi import FastAPI
from qdrant_client import QdrantClient

app = FastAPI()

# This uses the environment variable 'QDRANT_URL'  Testing the webhook
# We defined this in your docker-compose.yml as 'http://qdrant:6333'
QDRANT_URL = os.getenv("QDRANT_URL", "http://qdrant:6333")

@app.get("/health")
def health_check():
    try:
        # Initialize the client pointing to the Qdrant service
        client = QdrantClient(url=QDRANT_URL)
        
        # This makes a quick lightweight call to the Qdrant API
        client.get_collections()
        
        return {"status": "connected", "qdrant_url": QDRANT_URL}
    except Exception as e:
        return {"status": "error", "message": str(e)}