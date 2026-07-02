from langchain_core.messages import ToolMessage

from tools.calculator_tool import calculator


TOOLS = {
    "calculator": calculator
}


def execute_tool(tool_call):
    """
    Execute the tool requested by the LLM.
    """

    tool_name = tool_call["name"]
    tool_args = tool_call["args"]

    tool = TOOLS[tool_name]

    result = tool.invoke(tool_args)

    return ToolMessage(
        content=str(result),
        tool_call_id=tool_call["id"]
    )