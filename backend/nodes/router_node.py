from graph.state import PortfolioState


def router_node(state: PortfolioState) -> PortfolioState:
    question = state["question"].lower()

    portfolio_keywords = [
        "project",
        "projects",
        "portfolio",
        "resume",
        "experience",
        "skill",
        "skills"
    ]

    if any(keyword in question for keyword in portfolio_keywords):
        state["intent"] = "portfolio"
    else:
        state["intent"] = "chat"

    return state