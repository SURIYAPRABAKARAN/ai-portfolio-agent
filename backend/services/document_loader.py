from langchain_community.document_loaders import TextLoader


def load_resume():
    """
    Load the resume document.
    """

    loader = TextLoader(
        "data/resume.md",
        encoding="utf-8"
    )

    documents = loader.load()

    return documents

def split_documents(documents):
    """
    Split documents into smaller chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    return chunks