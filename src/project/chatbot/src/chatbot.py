from typing import Literal, Optional
from pydantic import BaseModel, ConfigDict, Field

class Message(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    role: Literal[ "user", "assistant"]
    content: str = Field(..., min_length=1, max_length=2000, description="The content of the message.")
    #ame: Optional[str] = Field(None, description="The name of the user or assistant sending the message.")

class ChatSession():
    def __init__(self):
        self.messages: list[Message] = []

    def add_message(self, role: str, content: str, name: Optional[str] = None):
        create_message = Message(role=role, content=content)
        
        if len(self.messages) >= 20:
            self.messages.pop(0)

        self.messages.append(create_message)

    def respond(self, messages: list[Message]) -> str:

        for message in reversed(messages):
            if message.role == "user":
                return f"Fake user message: {message.content}"
            
        return "No messages to respond to."
        
def chat(
    session: ChatSession,
    provider: FakeProvider,
    user_input: str
) -> str:
    session.add_message("user", user_input)
    response = provider.respond(session.messages)
    session.add_message("assistant", response)
    return response

class FakeProvider:
    def respond(self, messages: list[Message]) -> str:
        for message in reversed(messages):
            if message.role == "user":
                return f"Fake response to: {message.content}"

        return "No user message found"
    
if __name__ == "__main__":
    session = ChatSession()
    provider = FakeProvider()

    chat(session, provider, "What is RAG?")
    chat(session, provider, "Can you explain RAG in more detail?")

    print("\nConversation history:")
    for message in session.messages:
        print(f"{message.role}: {message.content}")