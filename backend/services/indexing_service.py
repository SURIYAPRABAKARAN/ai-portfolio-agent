from services.document_loader import load_resume
from services.text_splitter import split_documents
from services.vector_store import create_vector_store
from pathlib import Path


def index_resume():
    """
    Build the complete vector database from the resume.
    """

    print("Loading resume...")

    documents = load_resume()

    print(f"Loaded {len(documents)} document(s).")

    print("Splitting documents...")

    chunks = split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    print("Creating vector database...")

    create_vector_store(chunks)

    print("Indexing completed successfully!")
    
    
def initialize_vector_store():
    """
    Create the vector database only if it doesn't already exist.
    """

    chroma_path = Path("./chroma_db")

    if chroma_path.exists():
        print("ChromaDB already exists. Skipping indexing.")
        return

    print("ChromaDB not found. Building vector database...")

    index_resume()