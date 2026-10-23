
 
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

def test_chat_session_memory_limit():
    session = ChatSession()
    provider = FakeProvider()

    # Add 21 messages to exceed the limit of 20
    for i in range(25):
        user_input = f"Message {i + 1}"
        chat(session, provider, user_input)

    # Ensure only the last 20 messages are stored
    assert len(session.messages) == 20
    assert session.messages[0].content == "Message 16"  # The first message should be "Message 6"
    assert session.messages[-1].content == "Fake response to: Message 25"  # The last message should be the response to "Message 25"