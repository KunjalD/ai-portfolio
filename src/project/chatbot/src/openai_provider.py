from ast import List
from openai import OpenAI
from project.chatbot.src.chatbot import Message
import os

class OpenAIProvider:
    def __init__(self, api_key: str = None, client: OpenAI = None):
        if api_key is None:
            api_key = os.getenv("OPENAI_API_KEY")
        self.client = client if client is not None else OpenAI(api_key=api_key)

    def respond(self, messages: list[Message]) -> str:
        formated_messages = [message.model_dump()
            for message in messages]
        response = self.client.responses.create(
            model="gpt-4.1-mini",
            input=formated_messages)
        return response.output_text

class FakeResponse:
    output_text: str = "This is a fake response."

class FakeResponses:
    def create(self, model: str, input: List[dict]) -> FakeResponse:
        self.last_input = input
        return FakeResponse()

    def __init__(self, last_input: List[dict] = None):
        self.last_input = last_input
    
class FakeClient:
    def __init__(self):
        self.responses = FakeResponses()

if __name__ == "__main__":
    fake_client = FakeClient()
    respond = fake_client.responses.create(model="test", input=[]) 
    print(f"Fake response: {respond.output_text}")