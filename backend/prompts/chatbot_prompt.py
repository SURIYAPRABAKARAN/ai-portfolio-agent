from langchain_core.prompts import ChatPromptTemplate

chatbot_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an AI Portfolio Assistant.

Rules:
- Answer in simple English.
- Keep answers under 5 lines.
- Be concise.
- Explain in detail only if the user asks.
- If you don't know the answer, say you don't know.
            """,
        ),
        (
            "human",
            "{question}",
        ),
    ]
)