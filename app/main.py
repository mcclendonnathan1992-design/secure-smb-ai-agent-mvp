from fastapi import FastAPI

app = FastAPI(title="Secure SMB AI Agent", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok"}
