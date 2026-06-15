from groq import Groq
from app.config import settings

client = Groq(
    api_key=settings.GROQ_API_KEY
)


def generate_answer(
    question: str,
    context,
):
    prompt = f"""
You are NovaBite's business analytics assistant.

Question:
{question}

Data:
{context}

Rules:
1. Use ONLY the provided data.
2. Mention exact numbers.
3. Do not hallucinate.
4. Keep the answer concise.
5. If information is unavailable,
   say so.
"""

    response = (
        client.chat.completions.create(
            model=settings.MODEL_NAME,
            messages=[
                {
                    "role":
                    "system",
                    "content":
                    "You are a business analytics assistant."
                },
                {
                    "role":
                    "user",
                    "content":
                    prompt,
                },
            ],
            temperature=0,
        )
    )

    return (
        response
        .choices[0]
        .message
        .content
    )