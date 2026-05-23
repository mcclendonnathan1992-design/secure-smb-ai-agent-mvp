from fastapi import FastAPI, HTTPException
from app.schemas import AskRequest, AskResponse
from app.rag import retrieve
from app.llm import ask

app = FastAPI(title="Secure SMB AI Agent", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse)
def ask_endpoint(request: AskRequest):
    try:
        context = retrieve(request.question)
        answer = ask(request.question, context)
        return AskResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
