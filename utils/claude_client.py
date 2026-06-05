import os
import anthropic

DEFAULT_MODEL = "claude-haiku-4-5"

LENGTH_INSTRUCTIONS = {
    "Short": "Write a short summary in 50-75 words.",
    "Medium": "Write a medium-length summary in 150-200 words.",
    "Detailed": "Write a detailed summary in 300-400 words.",
}


def summarize_text(text: str, length_option: str, model: str = DEFAULT_MODEL) -> str:
    """Summarize text using the Claude API.

    Args:
        text: The text to summarize.
        length_option: One of "Short", "Medium", or "Detailed".
        model: Claude model ID to use.

    Returns:
        The generated summary string.
    """
    length_instruction = LENGTH_INSTRUCTIONS.get(length_option, LENGTH_INSTRUCTIONS["Medium"])

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    client = anthropic.Anthropic(api_key=api_key)

    message = client.messages.create(
        model=model,
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"{length_instruction}\n\nText to summarize:\n\n{text}",
            }
        ],
    )

    return message.content[0].text
