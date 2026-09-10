# app/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.retrieval import get_top_wines
from app.rag import build_context, generate_answer



app = FastAPI(
    title="Wine RAG API",
    description="RAG-based wine recommendation API",
    version="1.0.0"
)


class QueryRequest(BaseModel):
    query: str = Field(
        ...,
        min_length=3,
        description="Wine recommendation question"
    )



@app.get("/")
def root():
    return {
        "message": "Wine RAG API is running"
    }


@app.post("/query")
def query_wine(request: QueryRequest):

    try:
        user_query = request.query.strip()

        if not user_query:
            raise HTTPException(
                status_code=400,
                detail="Query cannot be empty"
            )

        # Retrieve relevant wines
        hits = get_top_wines(user_query)

        if not hits:
            raise HTTPException(
                status_code=400,
                detail="No relevant wines found"
            )

        # Build RAG context
        context = build_context(hits)

        # Generate answer using Gemini
        answer = generate_answer(
            user_query,
            context
        )

        return {
            "query": user_query,
            "answer": answer,
            "context": context
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occured while processing the request : {str(e)}"
        )





# # ------------------------------------
# # Get runtime query
# # ------------------------------------
# user_query = input(
#     "Enter your wine query: "
# )

#
# # ------------------------------------
# # Retrieve relevant wines
# # ------------------------------------
# hits = get_top_wines(user_query)
#
#
# # ------------------------------------
# # Build RAG context
# # ------------------------------------
# context = build_context(hits)
#
# # print("\nRetrieved Context:")
# # print(context)
#
#
# # ------------------------------------
# # Generate answer using Gemini
# # ------------------------------------
#
# answer = generate_answer(
#     user_query,
#     context
# )
#
#
# # ------------------------------------
# # Final answer
# # ------------------------------------
#
# print("\n================ FINAL ANSWER ================\n")
# print(answer)