# from services.ollama_service import get_llm

# llm = get_llm()

# response = llm.invoke(
#     "What is 25 * 40?"
# )

# print(response)

from services.ollama_service import get_llm
from services.tool_service import execute_tool

llm = get_llm()

messages = [
    ("human", "What is 125 * 40?")
]

response = llm.invoke(messages)

print(response)

if response.tool_calls:

    tool_message = execute_tool(
        response.tool_calls[0]
    )

    messages.append(response)
    messages.append(tool_message)

    final_response = llm.invoke(messages)

    print(final_response.content)