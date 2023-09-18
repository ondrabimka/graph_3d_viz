import uvicorn
from db.graph_conn import GraphConnClass
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

CORS_ALLOW_ORIGINS = ["http://localhost:3000", "localhost:8000", "localhost:8001"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

graph = GraphConnClass("memgraph", 7687, "", "")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/cypher_query")
def graph_query(query: str):
    return graph.get_graph_w_query(query)


@app.get("/get_whole_graph")
def get_whole_graph():
    return graph.get_whole_graph()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)
