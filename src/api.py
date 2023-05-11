from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

import gato.entity
import gato.llm
import gato.service

app = FastAPI()


class ScenarioRequest(BaseModel):
    parameters: gato.entity.ScenarioParameters
    prompt: gato.entity.ScenarioPrompt


class ScenarioResponse(BaseModel):
    scenario: gato.entity.Scenario


class ActionRequest(BaseModel):
    scenario: gato.entity.Scenario


class ActionResponse(BaseModel):
    action: gato.entity.Action


class DiscernRequest(BaseModel):
    scenario: gato.entity.Scenario
    choices: List[gato.entity.Action]


class DiscernResponse(BaseModel):
    action: gato.entity.Action
    explanation: str


class EvaluateRequest(BaseModel):
    scenario: gato.entity.Scenario
    action: gato.entity.Action
    result: str


class EvaluateResponse(BaseModel):
    success: bool
    explanation: str


class DecomposeRequest(BaseModel):
    action: gato.entity.Action


class DecomposeResponse(BaseModel):
    tasks: List[str]


@app.post("/scenario")
async def create_scenario(request: ScenarioRequest) -> ScenarioResponse:
    model = gato.llm.LLM("")
    gato_service = gato.service.GatoService(model)
    scenario = gato_service.create_scenario()
    return ScenarioResponse(scenario=scenario)


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
