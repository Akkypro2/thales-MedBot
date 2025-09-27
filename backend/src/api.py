from fastapi import FastAPI, HTTPException, Query, status
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ValidationError, Field
from typing import List, Dict, Any
from dotenv import load_dotenv
from src.embed import get_embedding
from src.vector_store import load_vectorstore
from src.rag_pipeline import build_rag, query_rag
from src.ingest_index import build_index

load_dotenv()
app= FastAPI()

origins= ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],
    allow_credentials= True,
    allow_methods= ["*"],
    allow_headers= ["*"]
)

@app.on_event("startup")
def run_onstartup():
    build_index()

embeddings= get_embedding()
vectorstore= load_vectorstore("vectorstore.faiss", embeddings)
pipeline= build_rag(vectorstore)

class ChatRequest(BaseModel):
    query: str
    conversation_history: List[Dict[str, Any]]= Field(default_factory= list)

    
@app.get("/ask")
def ask(query: str= Query(..., description="Enter your question!")):
    try:
        answer= query_rag(pipeline, query)
        return {"question": query, "answer": answer} 
    except Exception as e:
        raise HTTPException(status_code= 500, detail=str(e))

        
@app.post("/ask")
def ask_post(request: ChatRequest):
    try:
        answer= query_rag(pipeline, request.query)
        response= answer.get("result", "Sorry, I could not find an answer.")
        response_data = {
            "response": response,
            "sources": [] 
        }
        return response_data

    except ValidationError as e:
        print("VALIDATION ERROR DETAILS:", e.errors())
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=e.errors()
        )
    
    except Exception as e:
        raise HTTPException(status_code= 500, detail= str(e))

@app.get("/")
def root():
    return RedirectResponse(url="/docs")