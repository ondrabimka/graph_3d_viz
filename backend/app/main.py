import os

import uvicorn
from db.neo4j_conn import Neo4jConnClass
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

CORS_ALLOW_ORIGINS = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

graph = Neo4jConnClass()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/neo4j_query")
def neo4j_query(query: str):
    return graph.run(query).to_data_frame()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=os.getenv["FAST_API_PORT"])
