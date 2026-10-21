from pathlib import Path
from dotenv import load_dotenv
from anthropic import Anthropic
import os

load_dotenv(Path(__file__).resolve().parent.parent / ".env")
print("API key loaded:", bool(os.getenv("ANTHROPIC_API_KEY")))

client = Anthropic()
copyright_document = """
Copyright protection begins automatically when an original
work is fixed in a tangible form. Registration is not required
for copyright protection in the United States, but it can
provide additional legal benefits.
"""

def ask_from_document(question: str, document: str) -> str:
    # Step 1: Construct a prompt containing the document
    # Step 2: Instruct Claude to use only that document
    # Step 3: Call ask_claude(prompt)
    # Step 4: Return the answer
    prompt = f""" Only look for the answer in the provided document.
    If you cannot find the answer, respond with "I cannot find the answer in the provided document."
    Do not use any outside knowledge or information.
    Document:{document}
    Question:{question}"""
    
    return ask_claude(prompt)

def ask_claude(question):
    response = client.messages.create(
        model = "claude-opus-5",
        max_tokens=1024,
        messages=[{
                "role": "user",
                "content": question
            }] )

    # print("Stop reason:", response.stop_reason)
    # print("Output tokens:", response.usage.output_tokens)
    # print("Content types:", [block.type for block in response.content])

    answer = "\n".join(
        block.text
        for block in response.content
        if block.type == "text")

    return answer

def evaluate_with_llm(document: str, question: str, answer: str, expected_answer: str) -> bool:
    prompt = f"""
    You are an expert in evaluating the correctness of answers based on a given document.
    Document: {document}
    Question: {question}
    Answer: {answer}
    Expected Answer: {expected_answer}
    Evaluation rules:
    1. Check whether the actual answer correctly addresses the question.
    2. Check whether every factual claim in the answer is supported
    by the source document.
    3. If any factual claim is unsupported or contradicts the document,
    return False, even if the rest of the answer is correct.
    4. Do not use outside knowledge to verify claims.
    5. Return exactly True or False, with no explanation.
    """
    response = ask_claude(prompt)
    return response.strip().lower() == "true"

if __name__ == "__main__":
    print("TEST 1 — Supported question")
    print(ask_from_document(
        "Is copyright registration required for protection?", copyright_document
    ))
    print("\nTEST 2 — Unsupported question")
    print(ask_from_document("How much does copyright registration cost?", copyright_document))
    print("\nTEST 3 — Evaluate answer correctness")
    question = "Is copyright registration required for protection?"
    correct_answer = "No, copyright registration is not required."
    hallucinated_answer = (
        "Copyright registration is not required. "
        "The registration fee is $45."
    )
    expected_answer = "Registration is not required for copyright protection."
    is_correct = evaluate_with_llm(copyright_document, question, correct_answer, expected_answer)
    print(f"Is the correct answer correct? {is_correct}")
    is_correct = evaluate_with_llm(copyright_document, question, hallucinated_answer, expected_answer)
    print(f"Is the hallucinated answer correct? {is_correct}")