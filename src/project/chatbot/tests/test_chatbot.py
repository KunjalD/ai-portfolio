
 
from project.chatbot.src.chatbot import ChatSession, FakeProvider, chat
import pytest

def test_chat_stores_both_messages():
    session = ChatSession()
    provider = FakeProvider()

    user_input = "What is RAG?"
    response = chat(session, provider, user_input)

    assert len(session.messages) == 2
    assert session.messages[0].role == "user"
    assert session.messages[0].content == user_input
    assert session.messages[1].role == "assistant"
    assert session.messages[1].content == response