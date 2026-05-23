# Risk Register

| ID | Risk | Likelihood | Impact | Inherent Risk | Control(s) | Residual Risk | Owner | Status |
|----|------|-----------|--------|---------------|------------|---------------|-------|--------|
| R-01 | Prompt injection causes LLM to reveal system prompt or act outside scope | Medium | High | High | SC-01, SC-03 | Medium | Engineering | Open |
| R-02 | LLM response contains PII from retrieved documents | Medium | High | High | SC-02, SC-04 | Low | Engineering | Open |
| R-03 | Unauthorized access to `/ask` endpoint | Medium | High | High | SC-05 | Low | Engineering | Open |
| R-04 | Runaway API spend due to abuse or bug | Medium | Medium | Medium | SC-06 | Low | Engineering | Open |
| R-05 | Vulnerable dependency exploited in production | Low | High | Medium | SC-07 | Low | DevOps | Open |
| R-06 | API key leaked via logs or error messages | Low | High | Medium | SC-04, SC-08 | Low | Engineering | Open |
| R-07 | Model hallucination presents false policy as fact | High | Medium | High | SC-03 (grounding) | Medium | Product | Open |
| R-08 | Data poisoning via malicious document upload | Low | High | Medium | Document ingestion controls (planned) | Medium | Engineering | Open |
| R-09 | Insider threat — employee queries sensitive docs outside their role | Medium | Medium | Medium | SC-05, SC-04, RBAC (planned) | Medium | Security | Open |
| R-10 | LLM provider outage causes service unavailability | Medium | Medium | Medium | Fallback messaging, retry logic (planned) | Low | Engineering | Open |

## Risk Rating Definitions
- **Likelihood:** Low (<10% per year), Medium (10–40%), High (>40%)
- **Impact:** Low (minimal disruption), Medium (moderate harm or cost), High (significant harm, regulatory, or reputational)
- **Inherent Risk:** Pre-control rating = Likelihood × Impact
- **Residual Risk:** Post-control rating

## Review Cadence
This register is reviewed monthly by the Engineering and Security leads. All High residual risks require a documented remediation plan within 30 days of identification.
