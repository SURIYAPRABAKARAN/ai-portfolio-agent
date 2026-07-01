from typing import TypedDict


class PortfolioState(TypedDict):
    """
    Shared data that travels through the graph.
    Every node can read and update it.
    """
    question: str
    answer: str
    intent: str