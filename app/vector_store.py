import os
import pandas as pd

from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer

from app.config import QDRANT_URL, EMBEDDING_MODEL, QDRANT_API_KEY



# ------------------------------------------------
# Initialize Qdrant
# ------------------------------------------------
#print(QDRANT_URL)
qdrant = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
    timeout=60
)


#print(qdrant.get_collections())
# ------------------------------------------------
# Initialize embedding model
# ------------------------------------------------
encoder = SentenceTransformer(
    EMBEDDING_MODEL
)

