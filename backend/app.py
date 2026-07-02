from services.indexing_service import initialize_vector_store
from fastapi import FastAPI

from graph.graph import build_graph

initialize_vector_store()

app = FastAPI()

graph = build_graph()


@app.get("/")
def home():

    return {
        "message": "AI Portfolio Agent Running 🚀"
    }


@app.post("/chat")
def chat(request: dict):

    result = graph.invoke({

        "question": request["question"],

        "answer": ""

    })

    return {
        "answer": result["answer"]
    }