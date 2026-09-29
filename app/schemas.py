from pydantic import BaseModel, Field


class AssistantRequest(BaseModel):
    message: str = Field(min_length=2, max_length=3000)


class AssistantResponse(BaseModel):
    client_answer: str
    manager_hint: str
    source: str