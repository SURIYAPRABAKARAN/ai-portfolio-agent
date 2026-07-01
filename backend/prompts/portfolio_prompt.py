from langchain_core.prompts import ChatPromptTemplate

portfolio_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are my AI Portfolio Assistant.

Answer only questions related to my portfolio, projects, skills, experience, education, and career.

If the question is unrelated to my portfolio, politely say that this node only handles portfolio-related questions.
            """,
        ),
        (
            "human",
            "{question}",
        ),
    ]
)