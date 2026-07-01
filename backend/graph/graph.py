from langgraph.graph import StateGraph, START, END

from graph.state import PortfolioState
from nodes.router_node import router_node
from nodes.chatbot_node import chatbot_node
from nodes.portfolio_node import portfolio_node


# ==========================================
# Routing Function
# ==========================================
def route(state: PortfolioState) -> str:
    """
    Reads the intent from the state and tells LangGraph
    which node to execute next.
    """
    return state["intent"]


def build_graph():
    """
    Build and compile the LangGraph workflow.
    """

    # ==========================================
    # Create Graph Builder
    # ==========================================
    builder = StateGraph(PortfolioState)

    # ==========================================
    # Register Nodes
    # ==========================================
    builder.add_node("router", router_node)
    builder.add_node("chatbot", chatbot_node)
    builder.add_node("portfolio", portfolio_node)

    # ==========================================
    # Connect START -> Router
    # ==========================================
    builder.add_edge(START, "router")

    # ==========================================
    # Conditional Routing
    # ==========================================
    builder.add_conditional_edges(
        "router",
        route,
        {
            "chat": "chatbot",
            "portfolio": "portfolio",
        }
    )

    # ==========================================
    # Connect Nodes -> END
    # ==========================================
    builder.add_edge("chatbot", END)
    builder.add_edge("portfolio", END)

    # ==========================================
    # Compile Graph
    # ==========================================
    graph = builder.compile()

    return graph