# Generators

This module consists of two classes - `ScenarioGenerator` and `ActionGenerator` - that are responsible for the generation of `Scenario` and `Action` entities respectively.

### ScenarioGenerator

The `ScenarioGenerator` class takes a language model and a `ScenarioPrompt` as its parameters during initialization.

The main method in this class is `generate()`, which is an asynchronous method that generates a `Scenario` entity.
This method first creates system and user messages from the given `ScenarioPrompt`.
The user message consists of the parameter names and their corresponding values from the `ScenarioPrompt`.
These messages are added to a `ChatPrompt` which is then submitted to the language model.
The output from the language model, which is a string description, is used to create and return a new `Scenario` entity.

### ActionGenerator

Similar to `ScenarioGenerator`, the `ActionGenerator` class takes a language model and an `ActionPrompt` as its parameters during initialization.

The `generate()` method in this class is also asynchronous and works similarly to the one in `ScenarioGenerator`.
It generates an `Action` entity by creating system and user messages from the `ActionPrompt`, adding them to a `ChatPrompt`, and then submitting this to the language model.
The user message in this case is the description of the scenario from the `ActionPrompt`. The output from the language model is used to create and return a new `Action` entity.

In both these classes, the `generate()` method is asynchronous because it involves IO-bound tasks (i.e., making API calls to the language model), and using asynchronous programming allows for these tasks to be performed concurrently, which can significantly improve performance.

See the [`generator` module](../../src/gato/generator.py) for a full implementation.
