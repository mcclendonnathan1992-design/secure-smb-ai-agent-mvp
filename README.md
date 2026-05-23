# Secure SMB AI Agent MVP

A retrieval-augmented generation (RAG) agent designed for small-to-medium businesses, with security controls built in from day one.

## Features (planned)
- `/ask` endpoint: answers employee and customer questions grounded in company documents
- Prompt injection detection and blocking
- PII redaction before sending to the LLM
- Audit logging for all queries and responses
- Out-of-scope query rejection

## Quick Start

### Local development
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Docker
```bash
docker compose up --build
```

Visit `http://localhost:8000/health` to confirm the service is running.

### Run tests
```bash
pytest tests/ -v
```

## Project Structure
```
app/
  main.py          FastAPI application and route definitions
  rag.py           Document loading, chunking, embedding, retrieval
  security.py      Prompt injection detection, PII redaction, output sanitization
  schemas.py       Pydantic request/response models
data/
  sample_business_docs/   Placeholder SMB documents for development
tests/
  test_health.py
  test_ask.py
  test_prompt_injection.py
  test_data_leakage.py
```

## Environment Variables
Copy `.env.example` to `.env` and fill in values before running.

| Variable | Description |
|---|---|
| `ANTHROPIC_API_KEY` | API key for the LLM provider |
| `LOG_LEVEL` | Logging verbosity (default: `INFO`) |

## Security
See [SECURITY_CONTROLS.md](SECURITY_CONTROLS.md) for implemented controls and [RISK_REGISTER.md](RISK_REGISTER.md) for known risks and mitigations.
