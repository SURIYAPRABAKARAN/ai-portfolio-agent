from langgraph.graph import StateGraph, START, END

from graph.state import PortfolioState
from nodes.chatbot_node import chatbot_node


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
    builder.add_node(
        "chatbot",
        chatbot_node
    )

    # ==========================================
    # Connect START -> chatbot
    # ==========================================
    builder.add_edge(
        START,
        "chatbot"
    )

    # ==========================================
    # Connect chatbot -> END
    # ==========================================
    builder.add_edge(
        "chatbot",
        END
    )

    # ==========================================
    # Compile Graph
    # ==========================================
    graph = builder.compile()

    return graph