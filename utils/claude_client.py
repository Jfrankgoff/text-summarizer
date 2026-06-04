import ollama

LENGTH_INSTRUCTIONS = {
    "Short": "Write a short summary in 50-75 words.",
    "Medium": "Write a medium-length summary in 150-200 words.",
    "Detailed": "Write a detailed summary in 300-400 words.",
}


def summarize_text(text: str, length_option: str) -> str:
    length_instruction = LENGTH_INSTRUCTIONS.get(length_option, LENGTH_INSTRUCTIONS["Medium"])

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": f"{length_instruction}\n\nText to summarize:\n\n{text}"
            }
        ]
    )

    return response.message.content
