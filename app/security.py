import re
from fastapi import HTTPException

# Each tuple: (compiled pattern, label) — label used internally for logging/metrics only.
# Detection strategy: keyword + structural signals that strongly co-occur with attacks
# but rarely appear in legitimate SMB support questions.
#
# OWASP LLM Top 10 coverage:
#   LLM01 — Prompt Injection  (instruction override, persona hijack, delimiter injection)
#   LLM06 — Sensitive Information Disclosure  (system prompt extraction, bulk dump)

_RULES: list[tuple[re.Pattern, str]] = [
    # LLM01 — Instruction override
    (
        re.compile(r"ignore\s+(previous|all|prior)\s+instructions?", re.IGNORECASE),
        "instruction-override",
    ),
    # LLM01 + LLM06 — System prompt / instruction extraction
    (
        re.compile(
            r"(reveal|show|print|display|output)\s+(me\s+)?(your\s+)?"
            r"(system\s+prompt|system\s+instructions?|instructions?|prompt)",
            re.IGNORECASE,
        ),
        "system-prompt-extract",
    ),
    (
        re.compile(
            r"what\s+(is|are)\s+(your\s+)?(system\s+prompt|instructions?|prompt)",
            re.IGNORECASE,
        ),
        "system-prompt-extract",
    ),
    # LLM06 — Bulk document / data dump
    (
        re.compile(
            r"(print|list|dump|show|give\s+me)\s+all\s+"
            r"(documents?|files?|content|data|chunks?)",
            re.IGNORECASE,
        ),
        "bulk-dump",
    ),
    # LLM01 — Role / privilege escalation
    (
        re.compile(
            r"\bi\s+am\s+(the\s+)?"
            r"(ceo|admin|administrator|owner|developer|superuser|manager)\b",
            re.IGNORECASE,
        ),
        "role-escalation",
    ),
    (
        re.compile(
            r"\bas\s+(the\s+)?"
            r"(ceo|admin|administrator|owner|developer|superuser)\b",
            re.IGNORECASE,
        ),
        "role-escalation",
    ),
    # LLM01 — Persona hijack / jailbreak
    (
        re.compile(
            r"\bact\s+as\b|\bpretend\s+(you\s+are|to\s+be)\b|\byou\s+are\s+now\b",
            re.IGNORECASE,
        ),
        "persona-hijack",
    ),
    (
        re.compile(r"\bDAN\b|do\s+anything\s+now", re.IGNORECASE),
        "jailbreak",
    ),
    # LLM01 — Guardrail bypass ("bypass all security", "disable your guardrails", etc.)
    (
        re.compile(
            r"(override|bypass|disable|circumvent)\s+(\w+\s+)?"
            r"(safety|security|restrictions?|filters?|guardrails?)",
            re.IGNORECASE,
        ),
        "guardrail-bypass",
    ),
]


def validate_input(question: str) -> None:
    """Raise HTTP 400 if the question matches a known prompt-injection pattern.

    Called before RAG retrieval and LLM invocation so no tokens are spent
    on adversarial inputs.
    """
    for pattern, _ in _RULES:
        if pattern.search(question):
            raise HTTPException(
                status_code=400,
                detail="Request blocked: potential prompt injection detected.",
            )
