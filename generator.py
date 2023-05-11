import pathlib
import random

import entity


def read_list(path):
    with open(path, encoding='utf-8', errors='ignore') as infile:
        return infile.read().strip().split('\n')


class ParametersGenerator:
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


class PromptGenerator:
    _base_dir = pathlib.Path(__file__).parent
    _default_path = pathlib.Path(".config/scenario-system-messages.txt")

    def __init__(self, parameters: entity.ScenarioParameters,
                 path: pathlib.Path = _base_dir / _default_path):
        self._parameters = parameters
        self._system_message = random.choice(read_list(path))

    def generate(self) -> entity.ScenarioPrompt:
        instance = entity.ScenarioPrompt(
            system_message=self._system_message,
            parameters=self._parameters,
        )
        return instance
