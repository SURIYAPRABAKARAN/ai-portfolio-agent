from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv

load_dotenv()


def get_embedding_model() -> OllamaEmbeddings:
    """
    Create and return the Ollama embedding model.
    """

    return OllamaEmbeddings(
        model="nomic-embed-text"
    )


def create_embeddings(chunks):
    """
    Generate embeddings for all document chunks.

    Args:
        chunks: List of LangChain Document objects

    Returns:
        List of embedding vectors
    """

    embedding_model = get_embedding_model()

    texts = [chunk.page_content for chunk in chunks]

    embeddings = embedding_model.embed_documents(texts)

    return embeddings