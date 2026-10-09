from anthropic import Anthropic

client = Anthropic()


def ask_claude(question):
    response = client.messages.create(
    model = "claude-opus-5",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": question
    }] )

    prompt = f"""
    Answer the question using only the document below.
    If the document does not contain the answer, say
    "I cannot find the answer in the provided document."

    Document:
    {https://www.copyright.gov/forms/formtx.pdf}

    Question:
    {question}
    """

    print("Stop reason:", response.stop_reason)
    print("Output tokens:", response.usage.output_tokens)
    print("Content types:", [block.type for block in response.content])

    answer = "\n".join(
        block.text
        for block in response.content
        if block.type == "text")

    return answer

print(ask_claude("What is copyright registration?"))
