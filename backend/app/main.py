import uvicorn
from db.neo4j_conn import GraphConnClass
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

CORS_ALLOW_ORIGINS = ["http://localhost:3001", "localhost:8000", "localhost:8001"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

graph = GraphConnClass("localhost", 7687, "", "")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/neo4j_query")
def neo4j_query(query: str):
    return graph.run(query).to_data_frame()


# @app.get("/get_whole_graph")
def get_whole_graph():
    # return graph as json
    return graph.get_whole_graph()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8001)
