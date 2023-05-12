from . import entity, generator, llm, prompt


class GatoService:
    _scenario_prompt_factory = prompt.ScenarioPromptFactory()
    _action_prompt_factory = prompt.ActionPromptFactory()

    def __init__(self, model: llm.LLM):
        self._model = model

    def create_scenario(self) -> entity.Scenario:
        scenario_prompt = self._scenario_prompt_factory.new()
        scenario_generator = generator.ScenarioGenerator(self._model, scenario_prompt)
        return scenario_generator.generate()

    def create_action(self, scenario: entity.Scenario) -> entity.Action:
        action_prompt = self._action_prompt_factory.new(scenario)
        action_generator = generator.ActionGenerator(self._model, action_prompt)
        return action_generator.generate()
