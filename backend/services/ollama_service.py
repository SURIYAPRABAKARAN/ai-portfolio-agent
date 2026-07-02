import os

from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.messages import BaseMessage
from tools.calculator_tool import calculator

# Load environment variables
load_dotenv()


def get_llm():
    """
    Returns a configured Ollama LLM instance.
    """

    model_name = os.getenv("OLLAMA_MODEL")

    llm = ChatOllama(
        model=model_name,
        temperature=0,
        num_predict=256
    )
    
    llm = llm.bind_tools([
        calculator
    ])

    return llm

def ask_llm(messages: list[BaseMessage]):
    """
    Send formatted messages to the LLM and return the response.
    """

    llm = get_llm()

    return llm.invoke(messages)