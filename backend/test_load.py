from services.document_loader import load_resume
from services.text_splitter import split_documents
from services.embedding_service import create_embeddings
from services.vector_store import create_vector_store
from services.vector_store import get_retriever

# documents = load_resume()

# chunks = split_documents(documents)

# embeddings = create_embeddings(chunks)

# print(f"Total Chunks: {len(chunks)}")
# print(f"Total Embeddings: {len(embeddings)}")
# print(f"Embedding Dimension: {len(embeddings[0])}")

# print("\nFirst 10 Values:")
# print(embeddings[0][:10])
# ---------------------------------------------------------------------------------------
# documents = load_resume()

# chunks = split_documents(documents)

# vector_store = create_vector_store(chunks)

# print("Vector database created successfully!")

# ---------------------------------------------------------------------------------------


# retriever = get_retriever()

# documents = retriever.invoke("Where do you work?")

# for doc in documents:
#     print("=" * 50)
#     print(doc.page_content)
# ---------------------------------------------------------------------------------------

from services.vector_store import get_retriever

retriever = get_retriever()

docs = retriever.invoke("project")

for i, doc in enumerate(docs, 1):
    print("=" * 80)
    print(f"Chunk {i}")
    print(doc.page_content)