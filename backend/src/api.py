from fastapi import FastAPI, HTTPException, Query, status
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Dict, Any
from langchain_community.chat_message_histories import ChatMessageHistory
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

store_session: dict[ str, ChatMessageHistory]= {}
class ChatRequest(BaseModel):
    query: str
    conversation_history: List[Dict[str, Any]]= Field(default_factory= list)
    session_id: str 
    
@app.get("/ask")
def ask(query: str= Query(..., description="Enter your question!"), session_id: str= Query(..., description="Unique session ID-")):
    try:
        if session_id not in store_session:
            store_session[session_id]= ChatMessageHistory()
        history: ChatMessageHistory= store_session[session_id]
        message_history= history.messages
        history.add_user_message(query)
        answer= query_rag(pipeline, query, message_history)
        history.add_ai_message(answer)
        return {"question": query, "answer": answer} 
    except Exception as e:
        raise HTTPException(status_code= 500, detail=str(e))

        
@app.post("/ask")
def ask_post(request: ChatRequest):
    try:
        if request.session_id not in store_session:
            store_session[request.session_id]= ChatMessageHistory()
        history: ChatMessageHistory= store_session[request.session_id]
        message_history= history.messages
        history.add_user_message(request.query)
        answer= query_rag(pipeline, request.query, message_history)
        history.add_ai_message(answer)
        response= answer
        response_data = {
            "response": response,
            "sources": [] 
        }
        return response_data
    except Exception as e:
        raise HTTPException(status_code= 500, detail= str(e))

@app.get("/")
def root():
    return RedirectResponse(url="/docs")