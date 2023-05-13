# Language Models

We use a Language Model (LLM) to generate text based on given prompts.
The current version of this package supports a single LLM API, specifically OpenAI's newest language models.
However, we aim to support more LLM APIs in the future.
To facilitate this, the design attempts to accommodate future expansions with minimal changes.

The language model related functionality is encapsulated within two primary classes: `ChatPrompt` and `LLM`.

## Chat Prompt

The `ChatPrompt` class is a simple structure used to manage the messages passed to the LLM.
It exposes a `messages()` method that returns the current list of messages, and utility methods like `add_message()`, `add_system_message()`, and `add_user_message()`, which are used to add messages to the prompt.

## Large Language Model

The `LLM` class is the main interface for interacting with the Language Model. It is initialized with an OpenAI API key and a model name (defaulting to "gpt-3.5-turbo").
The class exposes a `submit()` method that takes a `ChatPrompt` object, and optional parameters like `temperature` and `max_retries`, and submits it to the LLM for completion.
The response is then processed and returned as a string.

Internally, `LLM` uses an `_query()` method to send the request to OpenAI and parse the response. If the query fails due to an error, the `submit()` method will retry the query up to `max_retries` times, with an exponential backoff strategy, before finally aborting.

While this approach is currently designed around OpenAI's chat-based completion model, it implies the eventual creation of something like a `SimplePrompt` that would align more with other LLM APIs.
The specifics will be deferred until the addition of a new model, at which point the abstraction will be re-evaluated.

See the [`llm` module](../../src/gato/llm.py) for a full implementation.
