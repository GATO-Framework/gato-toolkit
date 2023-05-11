from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

import entity

app = FastAPI()


class ScenarioRequest(BaseModel):
    parameters: entity.ScenarioParameters
    prompt: entity.ScenarioPrompt


class ScenarioResponse(BaseModel):
    scenario: entity.Scenario


class ActionRequest(BaseModel):
    scenario: entity.Scenario


class ActionResponse(BaseModel):
    action: entity.Action


class DiscernRequest(BaseModel):
    scenario: entity.Scenario
    choices: List[entity.Action]


class DiscernResponse(BaseModel):
    action: entity.Action
    explanation: str


class EvaluateRequest(BaseModel):
    scenario: entity.Scenario
    action: entity.Action
    result: str


class EvaluateResponse(BaseModel):
    success: bool
    explanation: str


class DecomposeRequest(BaseModel):
    action: entity.Action


class DecomposeResponse(BaseModel):
    tasks: List[str]


@app.get("/scenario/{scenario_id}")
async def scenario(scenario_id) -> ScenarioResponse:
    pass


@app.post("/scenario")
async def scenario(request: ScenarioRequest) -> ScenarioResponse:
    pass


@app.post("/action")
async def action(request: ActionRequest) -> ActionResponse:
    pass


@app.post("/discern")
async def discern(request: DiscernRequest) -> DiscernResponse:
    pass


@app.post("/evaluate")
async def evaluate(request: EvaluateRequest) -> EvaluateResponse:
    pass


@app.post("/decompose")
async def decompose(request: DecomposeRequest) -> DecomposeResponse:
    pass
