# Data Model

The `entity` module is where the data classes, or entities, for the application are defined.
These entities are used to represent the key objects that the system works with.
They are implemented using [Pydantic](https://docs.pydantic.dev/latest/), a Python library for data validation using Python type annotations.

Here's an overview of each entity:

- `ScenarioParameters`: This class represents the parameters used to generate a scenario. It includes attributes for the random word, scope, severity, region, category, and domain. Each of these attributes are strings.
- `ScenarioPrompt`: This class represents the prompt used to generate a scenario. It includes a system message, which provides instructions to the language model, and a `ScenarioParameters` object, which provides the specific parameters for the scenario.
- `Scenario`: This class represents a generated scenario. It includes a description of the scenario, which is a string, and a unique identifier (UUID), which is generated automatically when a new `Scenario` instance is created.
- `ActionPrompt`: This class represents the prompt used to generate a potential action for a given scenario. It includes a system message, which provides instructions to the language model, and a `Scenario` object, which provides the context for the action.
- `Action`: This class represents a potential action that could be taken in a given scenario. It includes a description of the action, which is a string, and a unique identifier (UUID), which is generated automatically when a new `Action` instance is created.

Each of these classes extends Pydantic's `BaseModel`, which provides functionality for data validation, serialization, and deserialization.
The use of Pydantic allows for strong typing of the model attributes, as well as automatic conversion between JSON and the model instances.

These entities are foundational to the workings of the GATO Toolkit, providing a structured way to represent the prompts used to generate scenarios and actions, and the scenarios and actions themselves.
By keeping them separate and well-defined, it allows for flexibility and clarity in how they are used throughout the rest of the system.

See the [`entity` module](../../src/gato/entity.py) for a full implementation.
