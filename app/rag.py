import re
from pathlib import Path

DOCS_DIR = Path(__file__).parent.parent / "data" / "sample_business_docs"
TOP_K = 3

_STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "is", "are", "was", "were", "be", "been",
    "have", "has", "had", "do", "does", "did", "will", "would", "could",
    "should", "may", "might", "not", "this", "that", "it", "its", "i",
    "my", "we", "our", "you", "your", "they", "their", "what", "how",
    "when", "where", "who", "which", "if", "as", "so", "up", "can",
}


def _tokenize(text: str) -> list[str]:
    tokens = re.findall(r"\b[a-z]{2,}\b", text.lower())
    return [t for t in tokens if t not in _STOPWORDS]


def _load_chunks() -> list[dict]:
    chunks = []
    for path in sorted(DOCS_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        # Split on level-1 and level-2 markdown headers so each section is its own chunk
        sections = re.split(r"\n(?=#{1,2} )", text)
        for section in sections:
            section = section.strip()
            if len(section.split()) >= 10:
                chunks.append({"text": section, "source": path.name})
    return chunks


# Loaded once at import time; small corpus so memory cost is negligible
_CHUNKS: list[dict] = _load_chunks()


def _score(query_tokens: list[str], chunk_text: str) -> float:
    """Term-frequency overlap: fraction of chunk tokens that match query tokens."""
    chunk_tokens = _tokenize(chunk_text)
    if not query_tokens or not chunk_tokens:
        return 0.0
    freq: dict[str, int] = {}
    for t in chunk_tokens:
        freq[t] = freq.get(t, 0) + 1
    return sum(freq.get(t, 0) / len(chunk_tokens) for t in set(query_tokens))


def retrieve(query: str, top_k: int = TOP_K) -> str:
    """Return the top-k most relevant document chunks as a single context string."""
    query_tokens = _tokenize(query)
    ranked = sorted(_CHUNKS, key=lambda c: _score(query_tokens, c["text"]), reverse=True)
    top = ranked[:top_k]
    return "\n\n---\n\n".join(f"[Source: {c['source']}]\n{c['text']}" for c in top)
