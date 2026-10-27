
 
from pydantic import ValidationError
from project.chatbot.src.chatbot import ChatSession, FakeProvider, Message, chat
import pytest
from project.chatbot.src.openai_provider import OpenAIProvider, FakeClient

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

def test_invalid_message_role():
    session = ChatSession()

    with pytest.raises(ValidationError):
        session.add_message("admin", "Hello")

def test_empty_message_rejected():
    session = ChatSession()

    with pytest.raises(ValidationError):
        session.add_message("user", "   ")

def test_openai_provider_uses_injected_client():
    fake_client = FakeClient()
    provider = OpenAIProvider(client=fake_client)

    messages = [Message(role="user", content="Explain RAG brifly.")]
    result = provider.respond(messages)

    assert result == "This is a fake response."
    assert len(fake_client.responses.last_input) == 1
    assert fake_client.responses.last_input[0]["role"] == "user"
    assert fake_client.responses.last_input[0]["content"] == "Explain RAG brifly."

def test_openai_provider_receives_conversation_history():
    fake_client = FakeClient()
    provider = OpenAIProvider(client=fake_client)

    messages = [
        Message(role="user", content="What is RAG?"),
        Message(role="assistant", content="RAG combines retrieval with generation."),
        Message(role="user", content="Explain it with an example?") ]

    provider.respond(messages)

    assert len(fake_client.responses.last_input) == 3
    assert fake_client.responses.last_input[0]["role"] == "user"
    assert fake_client.responses.last_input[0]["content"] == "What is RAG?"
    assert fake_client.responses.last_input[1]["role"] == "assistant"
    assert fake_client.responses.last_input[1]["content"] == "RAG combines retrieval with generation."
    assert fake_client.responses.last_input[2]["role"] == "user"
    assert fake_client.responses.last_input[2]["content"] == "Explain it with an example?"
    