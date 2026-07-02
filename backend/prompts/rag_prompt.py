# from langchain_core.prompts import ChatPromptTemplate

# rag_prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             """
# You are an AI Portfolio Assistant.

# Answer the user's question using ONLY the provided context.

# If the answer is not present in the context, reply:

# "I couldn't find that information in the portfolio."

# Context:
# {context}
#             """
#         ),
#         (
#             "human",
#             "{question}"
#         )
#     ]
# )

from langchain_core.prompts import ChatPromptTemplate

rag_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an AI Portfolio Assistant.

Use ONLY the context below to answer the user's question.

If the answer exists in the context,
answer naturally.

If it does not exist,
say:
"I couldn't find that information in the portfolio."

Context:

{context}
"""
        ),
        (
            "human",
            "{question}"
        )
    ]
)