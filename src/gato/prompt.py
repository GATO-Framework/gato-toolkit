import pathlib
import random

from . import entity


def read_file(path):
    with open(path, encoding="utf-8", errors="ignore") as file:
        return file.read()


def read_list(path):
    return read_file(path).strip().split('\n')


class ScenarioParametersFactory:
    _base_dir = pathlib.Path(__file__).parent
    _default_path = pathlib.Path(".config/scenario-params")

    def __init__(self, path: pathlib.Path = _default_path):
        self._path = path

    def _get_random_parameter(self, name: str):
        path = self._base_dir / self._path / f"{name}.txt"
        choices = read_list(path)
        return random.choice(choices)

    def new(self) -> entity.ScenarioParameters:
        return entity.ScenarioParameters(
            random_word=self._get_random_parameter("entropies"),
            scope=self._get_random_parameter("scopes"),
            severity=self._get_random_parameter("severities"),
            region=self._get_random_parameter("regions"),
            category=self._get_random_parameter("categories"),
            domain=self._get_random_parameter("domains"),
        )


class ScenarioPromptFactory:
    _base_dir = pathlib.Path(__file__).parent
    _default_path = pathlib.Path(".config/scenario-system-messages.txt")

    def __init__(self, path: pathlib.Path = _base_dir / _default_path):
        self._system_messages = read_list(path)

    def new(self, parameters: entity.ScenarioParameters) -> entity.ScenarioPrompt:
        return entity.ScenarioPrompt(
            system_message=random.choice(self._system_messages),
            parameters=parameters,
        )


class ActionPromptFactory:
    _base_dir = pathlib.Path(__file__).parent
    _default_path = pathlib.Path(".config/action-system-message.txt")

    def __init__(self, path: pathlib.Path = _base_dir / _default_path):
        self._system_message = read_file(path)

    def new(self, scenario: entity.Scenario) -> entity.ActionPrompt:
        return entity.ActionPrompt(
            system_message=self._system_message,
            scenario=scenario,
        )
