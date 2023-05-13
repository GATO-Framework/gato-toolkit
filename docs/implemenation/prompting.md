# Prompt Factories

Prompt factories are a crucial part of the `gato` package.
They are responsible for creating new prompts based on pre-made templates stored in the file system.
Currently, we have three main prompt factory classes: `ScenarioParametersFactory`, `ScenarioPromptFactory`, and `ActionPromptFactory`.
Each of these classes reads from one or more files to create new prompts.

### Scenario Parameters Factory

`ScenarioParametersFactory` is used to generate the parameters for a new scenario.
The parameters are stored in text files, each containing a list of possible options for a given parameter.
For instance, possible values for scope, severity, region, category, and domain are stored in their respective text files.
The factory reads these files, and a random value is chosen from each to form a `ScenarioParameters` entity.

### Scenario Prompt Factory

`ScenarioPromptFactory` generates a new scenario prompt, given the parameters.
It reads from a text file containing a list of system messages.
One of these messages is randomly selected to be part of the new `ScenarioPrompt`.
This factory takes an instance of `ScenarioParameters` as an argument and returns a `ScenarioPrompt` entity.

### Action Prompt Factory

`ActionPromptFactory` is responsible for generating prompts for potential actions an AI model might take in a given scenario.
It reads a single system message from a text file and pairs it with the given scenario to create an `ActionPrompt`.
The factory takes an instance of `Scenario` as an argument and returns an `ActionPrompt` entity.

These factories allow us to efficiently generate new, varied prompts by simply drawing from our pre-existing pool of possible values.
This design choice of keeping the prompt generation logic separate and encapsulated within these factories allows for greater modularity and ease of changes in the future.
As we move forward, we will certainly consider more options for prompt generation.

See the [`prompt` module](../../src/gato/prompt.py) for a full implementation.
