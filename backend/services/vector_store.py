from langchain_chroma import Chroma

from services.embedding_service import get_embedding_model


def create_vector_store(chunks):
    """
    Create and persist the Chroma vector database.
    """

    embedding_model = get_embedding_model()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="./chroma_db"
    )

    return vector_store


def load_vector_store():
    """
    Load an existing Chroma vector database.
    """

    embedding_model = get_embedding_model()

    vector_store = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embedding_model
    )

    return vector_store


def get_retriever():
    """
    Create a retriever from the vector store.
    """

    vector_store = load_vector_store()

    retriever = vector_store.as_retriever(
        search_kwargs={
            "k": 3
        }
    )

    return retriever