import uuid
from pydantic import BaseModel, Field


class ScenarioParameters(BaseModel):
    random_word: str
    scope: str
    severity: str
    region: str
    category: str
    domain: str


class ScenarioPrompt(BaseModel):
    system_message: str
    parameters: ScenarioParameters


class Scenario(BaseModel):
    description: str
    id: uuid.UUID = Field(default_factory=uuid.uuid4)


class ActionPrompt(BaseModel):
    system_message: str
    scenario: Scenario


class Action(BaseModel):
    description: str
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
