from pyexpat.errors import messages

from opentelemetry import context

from services.vector_store import get_retriever
from services.ollama_service import get_llm

from prompts.rag_prompt import rag_prompt


def generate_rag_response(question: str) -> str:
    """
    Retrieve relevant documents and generate an answer.
    """

    # ==========================================
    # Retrieve relevant documents
    # ==========================================
    retriever = get_retriever()

    documents = retriever.invoke(question)
    
    # ==========================================
    # Build context
    # ==========================================
    
    context = "\n\n".join(
        doc.page_content for doc in documents
    )

    # ==========================================
    # Build Prompt
    # ==========================================
    messages = rag_prompt.format_messages(
        context=context,
        question=question
    )


    # ==========================================
    # Call LLM
    # ==========================================
    llm = get_llm()
    
    response = llm.invoke(messages)

    return response.content