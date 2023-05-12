from . import entity, generator, llm, prompt


class GatoService:
    _scenario_parameters_factory = prompt.ScenarioParametersFactory()
    _scenario_prompt_factory = prompt.ScenarioPromptFactory()
    _action_prompt_factory = prompt.ActionPromptFactory()

    def __init__(self, model: llm.LLM):
        self._model = model

    def create_scenario_parameters(self) -> entity.ScenarioParameters:
        return self._scenario_parameters_factory.new()

    def create_scenario_prompt(
            self, parameters: entity.ScenarioParameters,
    ) -> entity.ScenarioPrompt:
        scenario_prompt = self._scenario_prompt_factory.new(parameters)
        return scenario_prompt

    def create_scenario(
            self, scenario_prompt: entity.ScenarioPrompt,
    ) -> entity.Scenario:
        scenario_generator = generator.ScenarioGenerator(self._model, scenario_prompt)
        return scenario_generator.generate()

    def create_action_prompt(self, scenario: entity.Scenario):
        return self._action_prompt_factory.new(scenario)

    def create_action(self, action_prompt: entity.ActionPrompt) -> entity.Action:
        action_generator = generator.ActionGenerator(self._model, action_prompt)
        return action_generator.generate()
