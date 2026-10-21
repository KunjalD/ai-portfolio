from typing import Protocol

class ChatProvider(Protocol):
    def reply(self, message: str) -> str:
        ...

class FakeProvider:
    def reply(self, message: str) -> str:
        return f"Fake response: {message}"

def chat(provider: ChatProvider):
    print(provider.reply("Hello"))

chat(FakeProvider())

