from . import entity, llm


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
