import entity
import generator
import llm


class GatoService:

    def __init__(self, model: llm.LLM):
        self._model = model

    def create_scenario(self) -> entity.Scenario:
        parameters_generator = generator.ScenarioParametersGenerator()
        parameters = parameters_generator.generate()
        prompt_generator = generator.ScenarioPromptGenerator(parameters)
        prompt = prompt_generator.generate()
        scenario_generator = generator.ScenarioGenerator(self._model, prompt)
        return scenario_generator.generate()

    def create_action(self):
        pass
