import os
from dotenv import load_dotenv

load_dotenv()


# -------------------------
# API Keys / URLs
# -------------------------

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")


# -------------------------
# Models
# -------------------------

GEMINI_MODEL = "gemini-2.5-flash"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


# -------------------------
# RAG settings
# -------------------------
TRAIN_FILE_NAME = "top_rated_wines.csv"
COLLECTION_NAME = "top_wines"

TOP_K = 3