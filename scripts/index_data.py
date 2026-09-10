import os
import pandas as pd

from qdrant_client import models

from app.vector_store import qdrant, encoder
from app.config import (
    COLLECTION_NAME,
    TRAIN_FILE_NAME
)



# ------------------------------------------------
# Build vector database
# ------------------------------------------------

def index_data():

    # Load data
    file_path = os.path.join(
        "Input CSVs",
        TRAIN_FILE_NAME
    )

    df_train = pd.read_csv(file_path)

    print("df_train =================")
    print(df_train.head())

    # Convert dataframe into records
    data = df_train.to_dict("records")

    # Delete existing collection if present
    if qdrant.collection_exists(
        collection_name=COLLECTION_NAME
    ):
        qdrant.delete_collection(
            collection_name=COLLECTION_NAME
        )

    print("xxxxxxxxxxx Deleted existing collection xxxxxxxxxxxxx")

    # Create collection
    qdrant.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(
            size=encoder.get_embedding_dimension(),
            distance=models.Distance.COSINE
        ),
    )
    print("=========== QDrant Collection Created ================")

    # Generate embeddings and upload
    qdrant.upload_points(
        collection_name=COLLECTION_NAME,
        points=[
            models.PointStruct(
                id=idx,
                vector=encoder.encode(doc["notes"]).tolist(),
                payload=doc
            )
            for idx, doc in enumerate(data)
        ]
    )

    print("########### Vector store initialized successfully. ##########################")

if __name__ == "__main__":
    index_data()