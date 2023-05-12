from typing import List, Annotated

from fastapi import FastAPI, Header
from pydantic import BaseModel

import gato.entity
import gato.llm
import gato.service

app = FastAPI()


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
async def create_scenario(api_key: Annotated[str, Header()]) -> ScenarioResponse:
    model = gato.llm.LLM(api_key)
    gato_service = gato.service.GatoService(model)
    scenario = gato_service.create_scenario()
    return ScenarioResponse(scenario=scenario)


@app.post("/action")
async def create_action(
        request: ActionRequest,
        api_key: Annotated[str, Header()],
) -> ActionResponse:
    model = gato.llm.LLM(api_key)
    gato_service = gato.service.GatoService(model)
    action = gato_service.create_action(request.scenario)
    return ActionResponse(action=action)


@app.post("/discern")
async def discern(request: DiscernRequest) -> DiscernResponse:
    pass


@app.post("/evaluate")
async def evaluate(request: EvaluateRequest) -> EvaluateResponse:
    pass


@app.post("/decompose")
async def decompose(request: DecomposeRequest) -> DecomposeResponse:
    pass
