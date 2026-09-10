model = "gemini-2.5-flash"
collection_name = "top_wines"

import os
from dotenv import load_dotenv

load_dotenv()

# Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Models
GEMINI_MODEL = "gemini-2.5-flash"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Data
TRAIN_FILE_NAME = "top_rated_wines.csv"


# Qdrant
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = "top_wines"
TOP_K = 3