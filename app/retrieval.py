# app/retrieval.py

from app.vector_store import qdrant, encoder

from app.config import COLLECTION_NAME, TOP_K


def get_top_wines(query, top_k=TOP_K):
    # Convert natural-language query into embedding
    query_vector = encoder.encode(query).tolist()

    # Search Qdrant
    response = qdrant.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=top_k,
        with_payload=True
    )

    hits = response.points

    # Debugging
    print(
        "############ Qdrant Search Results ############"
    )

    for hit in hits:
        print(
            f"ID: {hit.id}, Score: {hit.score}"
        )
        print(
            f"Wine Details: {hit.payload}\n"
        )

    return hits

