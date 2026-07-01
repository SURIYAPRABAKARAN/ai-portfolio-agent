from graph.state import PortfolioState
from services.ollama_service import get_llm


def chatbot_node(state: PortfolioState) -> PortfolioState:
    """
    Chatbot Node

    Reads question from state,
    calls Ollama,
    updates answer in state.
    """

    print("\n===== Chatbot Node Executed =====")

    question = state["question"]

    llm = get_llm()

    response = llm.invoke(question)

    return {
        "question": question,
        "answer": response.content
    }