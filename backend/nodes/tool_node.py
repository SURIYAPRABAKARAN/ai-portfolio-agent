from graph.state import PortfolioState

from services.tool_service import execute_tool


def tool_node(state: PortfolioState) -> PortfolioState:
    """
    Execute the tool requested by the LLM.
    """

    tool_calls = state.get("tool_calls", [])

    if not tool_calls:
        return state

    tool_message = execute_tool(tool_calls[0])

    state["messages"].append(tool_message)

    return state