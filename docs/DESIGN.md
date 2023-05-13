# Design and Architecture

## Asynchronous Programming
This library uses asynchronous programming because the heavy lifting is done by LLMs accessed via API.
Therefore, we are IO bound, and an asynchronous approach allows for significant performance gain.
We are leveraging the native `async`/`await` syntax for Python's `asyncio` module, so this can be a bit unfamiliar to some users.
If this is new to you, have a look at a [primer like this](https://mlwhiz.com/blog/2022/11/26/asyncio/).
While this approach adds some complexity, we believe the benefits of native asynchronous functionality are sufficiently convincing.

## Implementation
- [Language Models](implemenation/language-models.md)
- [Data Model](implemenation/data-model.md)
- [Prompting](implemenation/prompting.md)
- [Generators](implemenation/generators.md)
- [Services](implemenation/services.md)
