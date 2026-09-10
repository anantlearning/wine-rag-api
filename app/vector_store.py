import os
import pandas as pd

from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer

from app.config import QDRANT_URL, EMBEDDING_MODEL



# ------------------------------------------------
# Initialize Qdrant
# ------------------------------------------------
#print(QDRANT_URL)
qdrant = QdrantClient(
    url=QDRANT_URL,
    timeout=60
)


#print(qdrant.get_collections())
# ------------------------------------------------
# Initialize embedding model
# ------------------------------------------------
encoder = SentenceTransformer(
    EMBEDDING_MODEL
)

