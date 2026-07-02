from typing import TypedDict
from langchain_core.messages import BaseMessage


class PortfolioState(TypedDict):
    """
    Shared data that travels through the graph.
    Every node can read and update it.
    """
    question: str
    answer: str
    intent: str
    
    messages: list[BaseMessage]

    tool_calls: list