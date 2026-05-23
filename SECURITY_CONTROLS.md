# Security Controls

This document describes the security controls implemented (or planned) for the Secure SMB AI Agent.

## Control Categories

### SC-01 — Prompt Injection Prevention
**Status:** Planned
**Description:** All user-supplied input is scanned for known injection patterns (role-overriding instructions, system prompt extraction attempts, jailbreak keywords) before being passed to the LLM.
**Implementation:** `app/security.py` — `detect_prompt_injection()`
**Test coverage:** `tests/test_prompt_injection.py`

### SC-02 — PII Redaction
**Status:** Planned
**Description:** LLM responses are scanned for PII patterns (SSN, credit card numbers, email addresses, phone numbers) before being returned to the caller. Matches are redacted with `[REDACTED]`.
**Implementation:** `app/security.py` — `redact_pii()`
**Test coverage:** `tests/test_data_leakage.py`

### SC-03 — Retrieval Scope Enforcement
**Status:** Planned
**Description:** The RAG pipeline only retrieves from the approved document corpus. The LLM system prompt instructs the model to answer only from retrieved context and decline out-of-scope questions.
**Implementation:** `app/rag.py`, `app/main.py` system prompt

### SC-04 — Audit Logging
**Status:** Planned
**Description:** Every request and response is logged with a timestamp, sanitized user query (PII stripped), retrieved document chunks, and response. Logs are append-only and shipped to a SIEM.
**Implementation:** `app/main.py` middleware

### SC-05 — Authentication & Authorization
**Status:** Planned
**Description:** The `/ask` endpoint requires a valid API key passed in the `X-API-Key` header. Keys are validated against a secrets store (never hardcoded).
**Implementation:** `app/security.py` — `verify_api_key()`

### SC-06 — Rate Limiting
**Status:** Planned
**Description:** Each API key is limited to 60 requests per minute to prevent abuse and runaway LLM costs.
**Implementation:** FastAPI middleware or reverse proxy (nginx/Caddy)

### SC-07 — Dependency Scanning
**Status:** Active (CI)
**Description:** `pip audit` runs in CI on every push to detect known vulnerabilities in dependencies.
**Implementation:** `.github/workflows/python-ci.yml`

### SC-08 — Secrets Management
**Status:** Active
**Description:** Secrets are loaded from environment variables via `python-dotenv`. The `.env` file is gitignored. No secrets are hardcoded or logged.
**Implementation:** `app/main.py` startup, `.gitignore`
