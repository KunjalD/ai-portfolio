import sys


def get_answer():
    return "Real API response"


def chatbot():
    return get_answer()


def test_chatbot(monkeypatch):
    current_module = sys.modules[__name__]

    monkeypatch.setattr(
        current_module,
        "get_answer",
        lambda: "Fake API response"
    )

    assert chatbot() == "Fake API response"