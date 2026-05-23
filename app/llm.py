from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

_client = Anthropic()  # reads ANTHROPIC_API_KEY from env

MODEL = "claude-sonnet-4-6"

_SYSTEM_PROMPT = (
    "You are a helpful assistant for a small business. "
    "Answer questions using only the provided context from company documents. "
    "If the answer is not in the context, say so clearly — do not invent information."
)


def ask(question: str, context: str = "") -> str:
    content = f"Context:\n{context}\n\nQuestion: {question}" if context else question

    with _client.messages.stream(
        model=MODEL,
        max_tokens=1024,
        system=[
            {
                "type": "text",
                "text": _SYSTEM_PROMPT,
                "cache_control": {"type": "ephemeral"},  # cache stable system prompt
            }
        ],
        messages=[{"role": "user", "content": content}],
    ) as stream:
        return stream.get_final_message().content[0].text
