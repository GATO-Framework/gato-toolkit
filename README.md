# GATO Toolkit: An open-source toolkit for AI alignment

> NOTE: This project is **unstable**, you should consider all functionality *experimental* and *subject to change* without warning.

This project is intended to further research in AI alignment and the control problem.
In particular, the approach adopted here is inspired by the [GATO Framework](https://www.gatoframework.org/),
a comprehensive methodology for promoting positive intentions in AI systems worldwide.

As this is an ongoing effort, the GATO Toolkit will evolve along with the research.
In this current iteration, the focus is on dataset generation and model alignment.

## Capabilities

### Come up with new scenarios to test
You can generate all kinds of scenarios ranging from inconsequential personal problems to catastrophic global disasters.
These scenarios serve as the basis for new investigations.

### Determine an appropriate action for any scenario
Once you've got a scenario, you can ask the model how it would attempt to handle the situation.

### Compare different actions to see which is most aligned
Given a particular scenario, you can provide a number of different possible actions to see which one the model believes
is best aligned with the heuristic imperatives.

### Evaluate the suitability of an action based on its consequences
Given a particular scenario, action, and result, you can ask the model to assess the effectiveness of that action and
reflect on the repercussions of that action.

### Break actions down into manageable tasks
Starting with a broad action plan, you can have the model break things up into a list of tasks that would be needed
to execute that plan.

## Usage

This project provides a library of functions that may be useful for all sorts of research tasks in AI alignment.
This functionality can be used directly in Python applications, but we also support two additional interfaces:
- [GATO Toolkit API](https://github.com/FyZyX/gato-toolkit-api)
- [GATO Toolkit UI](https://github.com/FyZyX/gato-toolkit-ui)

- If you want to develop new applications in Python, this library is probably the right choice. Jump straight to the [examples](#examples)! 
- But, if you're using a different programming langauge, the API will be your best bet.
- Finally, if you just want to leverage the existing functionality, have a look at the UI.

- Also, both of those resources serve as example usage code, so go take a look! 👀

If you do want to use this library directly, you'll probably want to interact with `GatoService` class.
You'll find the essential operations there, and you can see how the lower-level components work by examining the code in [`gato/service.py`](src/gato/service.py).

For more information on design and architecture, check out our [design doc](docs/DESIGN.md).

## Examples

### Generate a Scenario
```python
import gato.llm
import gato.service

async def generate_scenario(api_key: str):
    model = gato.llm.LLM(api_key)
    service = gato.service.GatoService(model)
    params = service.create_scenario_parameters()
    prompt = service.create_scenario_prompt(params)
    return await service.create_scenario(prompt)
```

### Generate an Action
```python
import gato.entity
import gato.llm
import gato.service

async def generate_action(api_key: str, scenario: gato.entity.Scenario):
    model = gato.llm.LLM(api_key)
    service = gato.service.GatoService(model)
    prompt = service.create_action_prompt(scenario)
    return await service.create_action(prompt)
```

## Additional Resources

- [GATO Framework](https://www.gatoframework.org/)
- [Reinforcement Learning with Heuristic Imperatives](https://github.com/daveshap/RLHI)

## Contributing

Contributions to the GATO Toolkit are welcome! Please read our [contributing guidelines](docs/CONTRIBUTING.md) and [code of conduct](docs/CODE-OF-CONDUCT.md) before you start.

## License

[MIT](https://choosealicense.com/licenses/mit/)
