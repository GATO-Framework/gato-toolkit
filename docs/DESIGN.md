# Design and Architecture

## Language Models
Currently, we only support a single LLM API, but we expect to expand this over time.
Theoretically, user's should be able to configure their language model and inject into the necessary service.

To that end, we have tried to design with this future in mind, but some immediate challenges make this difficult.
In particular, the chat message format of the OpenAI API makes abstraction significantly more cumbersome.
At this stage, our approach is to use a `ChatPrompt` class that exposes a `messages()` method (as well as some utility methods for adding messages by role).
This is intended to imply the eventual existence of something like a `SimplePrompt` that would align more with other LLM APIs.
Util we actually add a new model, we've decided to defer this level of abstraction.

See the [`llm` module](../src/gato/llm.py) for specifics.

## Data Model
We've chosen to use [Pydantic](https://docs.pydantic.dev/latest/) for our data classes, which we call **entities**.
We've chosen to model both the result models, like `Scenario` and `Action`, but also the prompts that produce these entities, like `ScenarioPrompt` and `ActionPrompt`.
These models are fairly simple right now, and they may not need to be too much more complicated, but we may want to add some additional attributes down the line.

One big design choice at this stage is not to model relationships between the entities because it is unclear how we want to persist these structures long term.
That means the onus is on the consumer to keep track of which actions go with which scenario, etc.
This is okay because the service object makes these relationships explicit, so it is simply a matter of decorating any persistent structures in the client application.
Additionally, the relationships are implicitly specified in the prompt entities.
However, at some point it will probably be valuable to include these relationships explicitly in the data model, but only once a preferred persistence strategy has been established. 

See the [`entity` module](../src/gato/entity.py) for specifics.

## Asynchronous Programming
This library uses asynchronous programming because the heavy lifting is done by LLMs accessed via API.
Therefore, we are IO bound, and an asynchronous approach allows for significant performance gain.
We are leveraging the native `async`/`await` syntax for Python's `asyncio` module, so this can be a bit unfamiliar to some users.
If this is new to you, have a look at a [primer like this](https://mlwhiz.com/blog/2022/11/26/asyncio/).
While this approach adds some complexity, we believe the benefits of native asynchronous functionality are sufficiently convincing.
