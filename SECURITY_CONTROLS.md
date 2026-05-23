# Security Controls

| ID | Risk Addressed | Control | OWASP LLM Top 10 | Test File | Status |
|----|---------------|---------|------------------|-----------|--------|
| SC-01 | Prompt injection — instruction override | Pattern-based input guard rejects "ignore previous/all/prior instructions" before any RAG or LLM call (`app/security.py`) | LLM01 — Prompt Injection | `tests/test_prompt_injection.py` | ✅ Active |
| SC-02 | Prompt injection — system prompt extraction | Input guard blocks "reveal/show/print/display your system prompt", "what are your instructions?" and variants (`app/security.py`) | LLM01 — Prompt Injection, LLM06 — Sensitive Information Disclosure | `tests/test_prompt_injection.py`, `tests/test_data_leakage.py` | ✅ Active |
| SC-03 | Bulk document exfiltration | Input guard blocks "print/list/dump/show/give me all documents/files/content/data" (`app/security.py`) | LLM06 — Sensitive Information Disclosure | `tests/test_data_leakage.py` | ✅ Active |
| SC-04 | Role / privilege escalation | Input guard blocks "I am the CEO/admin/owner/developer" and "as the administrator/superuser" claim patterns (`app/security.py`) | LLM01 — Prompt Injection | `tests/test_prompt_injection.py` | ✅ Active |
| SC-05 | Persona hijack / jailbreak | Input guard blocks "act as", "pretend you are", "you are now DAN", "do anything now" (`app/security.py`) | LLM01 — Prompt Injection | `tests/test_prompt_injection.py` | ✅ Active |
| SC-06 | Guardrail bypass | Input guard blocks "override/bypass/disable/circumvent [your/all] safety/security/guardrails/restrictions" (`app/security.py`) | LLM01 — Prompt Injection | `tests/test_prompt_injection.py` | ✅ Active |
| SC-07 | Model hallucination / overreliance | RAG grounds every answer in retrieved document chunks; system prompt instructs Claude to refuse out-of-scope questions and never invent information (`app/rag.py`, `app/llm.py`) | LLM09 — Overreliance | `tests/test_data_leakage.py` | ✅ Active |
| SC-08 | Insecure output / schema leakage | Pydantic `AskResponse` enforces `{answer, sources}` — internal context strings, chunk metadata, and RAG markers cannot appear in the API response (`app/schemas.py`) | LLM02 — Insecure Output Handling | `tests/test_data_leakage.py` | ✅ Active |
| SC-09 | Empty / malformed input | Pydantic `AskRequest` enforces `min_length=1`; missing fields and wrong types return HTTP 422 before any processing or LLM spend (`app/schemas.py`) | LLM01 — Prompt Injection | `tests/test_ask.py` | ✅ Active |
| SC-10 | Secrets exposure | `ANTHROPIC_API_KEY` loaded from `.env` (gitignored); `.env.example` committed as template; no secrets hardcoded or logged (`app/llm.py`, `.gitignore`) | LLM06 — Sensitive Information Disclosure | — | ✅ Active |
| SC-11 | Container privilege escalation | Docker image runs as non-root `appuser`; data directory mounted read-only in Compose (`Dockerfile`, `docker-compose.yml`) | — | — | ✅ Active |
| SC-12 | PII in LLM responses | Output scanning for SSN, credit-card, email, phone patterns; matches redacted to `[REDACTED]` before returning to caller | LLM06 — Sensitive Information Disclosure | `tests/test_data_leakage.py` | 🔲 Planned |
| SC-13 | Unauthorized API access | Per-request API key validation via `X-API-Key` header; keys stored in secrets manager, never hardcoded | LLM01 — Prompt Injection | — | 🔲 Planned |
| SC-14 | API abuse / runaway LLM cost | Per-key rate limiting (60 req/min) at reverse proxy or FastAPI middleware | — | — | 🔲 Planned |
| SC-15 | Vulnerable dependencies | `pip-audit` in CI on every push; merge blocked on known CVEs | — | CI workflow | 🔲 Planned |

## OWASP LLM Top 10 Coverage

| Category | Active Controls | Planned Controls |
|----------|----------------|-----------------|
| LLM01 — Prompt Injection | SC-01, SC-02, SC-04, SC-05, SC-06, SC-09 | SC-13 |
| LLM02 — Insecure Output Handling | SC-08 | — |
| LLM06 — Sensitive Information Disclosure | SC-02, SC-03, SC-10, SC-11 | SC-12 |
| LLM09 — Overreliance | SC-07 | — |
