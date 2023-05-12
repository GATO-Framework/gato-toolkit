import pathlib
import random

import entity
import llm


def read_file(path):
    with open(path, encoding="utf-8", errors="ignore") as file:
        return file.read()


def read_list(path):
    return read_file(path).strip().split('\n')


class ScenarioParametersGenerator:
    _base_dir = pathlib.Path(__file__).parent
    _default_path = pathlib.Path(".config/scenario-params")

    def __init__(self, path: pathlib.Path = _default_path):
        self._path = path

    def _get_random_parameter(self, name: str):
        path = self._base_dir / self._path / f"{name}.txt"
        choices = read_list(path)
        return random.choice(choices)

    def generate(self) -> entity.ScenarioParameters:
        return entity.ScenarioParameters(
            random_word=self._get_random_parameter("entropies"),
            scope=self._get_random_parameter("scopes"),
            severity=self._get_random_parameter("severities"),
            region=self._get_random_parameter("regions"),
            category=self._get_random_parameter("categories"),
            domain=self._get_random_parameter("domains"),
        )


class ScenarioPromptGenerator:
    _base_dir = pathlib.Path(__file__).parent
    _default_path = pathlib.Path(".config/scenario-system-messages.txt")

    def __init__(self, parameters: entity.ScenarioParameters,
                 path: pathlib.Path = _base_dir / _default_path):
        self._parameters = parameters
        self._system_message = random.choice(read_list(path))

    def generate(self) -> entity.ScenarioPrompt:
        return entity.ScenarioPrompt(
            system_message=self._system_message,
            parameters=self._parameters,
        )


class ScenarioGenerator:

    def __init__(self, model: llm.LLM, prompt: entity.ScenarioPrompt):
        self._model = model
        self._prompt = prompt

    def generate(self) -> entity.Scenario:
        system_message = self._prompt.system_message
        parameters = self._prompt.parameters.dict().items()
        user_message = "\n".join([f"{name}: {param}" for name, param in parameters])

        prompt = llm.ChatPrompt()
        prompt.add_system_message(system_message)
        prompt.add_user_message(user_message)
        description = self._model.submit(prompt)
        return entity.Scenario(description=description)


class ActionPromptGenerator:
    _base_dir = pathlib.Path(__file__).parent
    _default_path = pathlib.Path(".config/scenario-params")

    def __init__(self, scenario: entity.Scenario, path: pathlib.Path = _default_path):
        self._path = path
        self._scenario = scenario

    def generate(self) -> entity.ActionPrompt:
        system_message = read_file(self._path)
        return entity.ActionPrompt(
            system_message=system_message,
            scenario=self._scenario,
        )


class ActionGenerator:

    def __init__(self, model: llm.LLM, prompt: entity.ActionPrompt):
        self._model = model
        self._prompt = prompt

    def generate(self) -> entity.Action:
        system_message = self._prompt.system_message
        scenario_description = self._prompt.scenario.description

        prompt = llm.ChatPrompt()
        prompt.add_system_message(system_message)
        prompt.add_user_message(scenario_description)
        description = self._model.submit(prompt)
        return entity.Action(description=description)
