# Services

The `GatoService` class serves as the main entry point for the functionality provided by the Gato toolkit. It provides a simplified interface for the generation of scenarios and actions, abstracting the details of the underlying components. This class uses the factory objects and generator classes defined in the toolkit to perform its tasks.

## Initialization

On instantiation, the `GatoService` class requires a language model of type `LLM`. This language model is used throughout the service for generating both scenarios and actions.

## Scenario Generation

The process of generating a scenario is divided into several steps that are each handled by a different method in the `GatoService` class:

1. `create_scenario_parameters`: This method utilizes the `ScenarioParametersFactory` to create a new `ScenarioParameters` object. This object contains the parameters that will guide the generation of a scenario.
2. `create_scenario_prompt`: This method takes the generated `ScenarioParameters` object and uses the `ScenarioPromptFactory` to produce a `ScenarioPrompt` object. This object represents the prompt that will be fed into the language model to generate a scenario.
3. `create_scenario`: This asynchronous method receives a `ScenarioPrompt` object and uses the `ScenarioGenerator` to generate a `Scenario` object. This object represents the generated scenario and contains the scenario text and unique ID.

## Action Generation

The process of generating actions is similarly divided into steps:

1. `create_action_prompt`: This method takes a `Scenario` object and uses the `ActionPromptFactory` to produce an `ActionPrompt` object. This object represents the prompt that will be used to generate potential actions for the provided scenario.
2. `create_action`: This asynchronous method receives an `ActionPrompt` object and uses the `ActionGenerator` to generate an `Action` object. This object represents the generated action and contains the action text and unique ID.

The service object makes explicit the relationships between the different components involved in the generation process, providing a clear and easy-to-use interface for generating scenarios and actions.

See the [`service` module](../../src/gato/service.py) for a full implementation.
