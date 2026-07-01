from graph.state import PortfolioState

from services.ollama_service import get_llm
from prompts.portfolio_prompt import portfolio_prompt


def portfolio_node(state: PortfolioState) -> PortfolioState:
    print("\n===== Portfolio Node Executed =====")

    question = state["question"]

    llm = get_llm()

    messages = portfolio_prompt.format_messages(
        question=question
    )

    response = llm.invoke(messages)

    state["answer"] = response.content

    return state