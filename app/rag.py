# app/rag.py

def build_context(hits):

    context = []

    for i, hit in enumerate(hits, start=1):

        context.append(
            f"""
        Wine {i}
        Similarity Score: {hit.score}
        Details: {hit.payload}
        """
        )

    return "\n".join(context)


# app/rag.py

from google import genai

from app.config import GEMINI_API_KEY, GEMINI_MODEL


client = genai.Client(
    api_key=GEMINI_API_KEY
)



def generate_answer(user_query, context):

    prompt = f"""
You are a knowledgeable wine specialist.

The user has asked:

{user_query}

Below is information retrieved from a wine database:

{context}

Using ONLY the retrieved information above:

1. Recommend the wine that best matches the user's request.
2. Explain why it is a good match.
3. Mention relevant details such as rating, price, variety,
   country or region when available.

Do not invent information that is not present in the retrieved data.

If the retrieved information is insufficient to answer the question,
say so clearly.
"""

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt
    )

    return response.text