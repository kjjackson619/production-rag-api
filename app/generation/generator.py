from openai import OpenAI
from app.config import settings


client = OpenAI(api_key=settings.OPENAI_API_KEY)

PROMPT_TEMPLATE = """
You are a helpful assitant.

Answer the question using ONLY the context below.
If the answer is not in the context, say "I don't know."

Context:
{context}


Question:
{question}
"""

def generate_answer(context: str, question: str):
    prompt = PROMPT_TEMPLATE.format(
        context=context,
        question=question
    )

    response = client.chat.completions.create(
        model=settings.GENERATION_MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content