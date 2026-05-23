# Risk Register

| ID | Risk | Likelihood (1–5) | Impact (1–5) | Inherent Score | Control(s) | Residual Score | Owner | Status |
|----|------|:----------------:|:------------:|:--------------:|------------|:--------------:|-------|--------|
| R-01 | Prompt injection causes LLM to ignore scope, reveal system prompt, or act as a different persona | 3 — Medium | 4 — High | 12 | SC-01, SC-02, SC-04, SC-05, SC-06 | 3 — Low | Engineering | ✅ Mitigated |
| R-02 | LLM response contains PII scraped from retrieved documents (SSN, email, phone) | 3 — Medium | 4 — High | 12 | SC-08, SC-12 (planned) | 8 — Medium | Engineering | ⚠️ Open |
| R-03 | Unauthenticated caller queries the `/ask` endpoint and extracts proprietary business information | 4 — High | 4 — High | 16 | SC-13 (planned) | 12 — High | Engineering | ⚠️ Open |
| R-04 | Runaway LLM API spend caused by abuse, loop bug, or missing rate limit | 3 — Medium | 3 — Medium | 9 | SC-14 (planned) | 6 — Medium | Engineering | ⚠️ Open |
| R-05 | Known CVE in a Python dependency exploited in production container | 2 — Low | 4 — High | 8 | SC-15 (planned), SC-11 | 4 — Low | DevOps | ⚠️ Open |
| R-06 | `ANTHROPIC_API_KEY` or other secret leaked via logs, error response, or git commit | 2 — Low | 5 — Critical | 10 | SC-10 | 2 — Low | Engineering | ✅ Mitigated |
| R-07 | Model hallucination presents invented policy details as authoritative fact | 4 — High | 3 — Medium | 12 | SC-07 (RAG grounding) | 6 — Medium | Product | ✅ Mitigated |
| R-08 | Data poisoning via a malicious document injected into the corpus at ingest time | 2 — Low | 4 — High | 8 | Document allowlist and hash verification (planned) | 6 — Medium | Engineering | ⚠️ Open |
| R-09 | Insider threat — authenticated employee queries documents outside their role (e.g., salary data) | 3 — Medium | 3 — Medium | 9 | SC-13 (planned), RBAC (planned) | 6 — Medium | Security | ⚠️ Open |
| R-10 | Anthropic API outage causes complete service unavailability with no fallback | 3 — Medium | 3 — Medium | 9 | Health-check endpoint; graceful HTTP 500 with user-facing message; retry/fallback (planned) | 6 — Medium | Engineering | ⚠️ Open |

## Risk Score Scale

| Score | Rating | Action |
|-------|--------|--------|
| 1–4 | Low | Accept; monitor at quarterly review |
| 5–9 | Medium | Mitigate within next sprint |
| 10–14 | High | Mitigate within 30 days; document plan |
| 15–25 | Critical | Immediate escalation; block release |

## Likelihood / Impact Definitions

**Likelihood**
| Rating | Definition |
|--------|-----------|
| 1 — Very Low | Unlikely; < 5% chance per year |
| 2 — Low | Possible; 5–15% chance per year |
| 3 — Medium | Plausible; 15–40% chance per year |
| 4 — High | Probable; 40–70% chance per year |
| 5 — Very High | Near-certain; > 70% chance per year |

**Impact**
| Rating | Definition |
|--------|-----------|
| 1 — Negligible | No user-facing effect |
| 2 — Minor | Degraded experience; no data loss |
| 3 — Medium | Service disruption or moderate data exposure |
| 4 — High | Significant data breach, regulatory exposure, or reputational harm |
| 5 — Critical | Severe financial, legal, or safety consequences |

## Review Cadence

This register is reviewed monthly by Engineering and Security leads. Any risk with a residual score ≥ 10 requires a written remediation plan within 30 days of identification.
