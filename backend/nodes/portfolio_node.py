from graph.state import PortfolioState

from services.rag_service import generate_rag_response


def portfolio_node(state: PortfolioState) -> PortfolioState:
    print("\n===== Portfolio Node Executed =====")

    question = state["question"]

    answer = generate_rag_response(question)

    state["answer"] = answer

    return state