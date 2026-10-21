from pydantic import BaseModel, Field, ValidationError
from typing import Literal

class Message(BaseModel):
    role: Literal["user", "assistant"]
    content: str = Field(min_length=1)

message = Message(role="user", content="Hello")
print(message.model_dump())

try:
    Message(role="admin", content="")
except ValidationError:
    print("Validation failed")

