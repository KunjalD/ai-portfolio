from src.first_response import ask_claude, ask_from_document
import re
 
document = """
Copyright protection begins automatically when an original work is fixed in a tangible form. Registration is not required for copyright protection in the United States, but it can provide additional legal benefits.
"""

def test_supported_question():
    question = "Is copyright registration required for protection?"
    expected_answer = "Copyright registration is not required for protection in the United States."
    answer = ask_from_document(question, document)
    assert expected_answer in answer

def test_unsupported_question():
    question = "How much does copyright registration cost?"
    expected_answer = "I cannot find the answer in the provided document."
    answer = ask_from_document(question, document)
    assert expected_answer in answer    

def test_unsupported_question():
    question = "How much does copyright registration cost?"
    answer = ask_from_document(question, document)          
    assert re.search(r"\$\d+", answer) is None, "Answer contains a dollar amount: {answer}"
    assert  "$" not in answer
