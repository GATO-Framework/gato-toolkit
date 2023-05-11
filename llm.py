import time

import openai as openai


class ChatPrompt:
    def __init__(self):
        self._messages: list[dict[str, str]] = []

    def add_message(self, role: str, content: str):
        self._messages.append({"role": role, "content": content})

    def add_system_message(self, content: str):
        self.add_message("system", content)

    def add_user_message(self, content: str):
        self.add_message("user", content)

    def messages(self):
        return self._messages


class LLM:
    def __init__(self, api_key, model_name: str = "gpt-3.5-turbo"):
        openai.api_key = api_key
        self._model_name = model_name

    def _query(self, prompt: ChatPrompt, **kwargs) -> str:
        response = openai.ChatCompletion.create(
            model=self._model_name,
            messages=prompt.messages(),
            **kwargs,
        )
        return response.choices[0]["message"]["content"]

    def submit(self, prompt: ChatPrompt, temperature: float = 0.7,
               max_retries: int = 3, **kwargs) -> str:
        for retry in range(max_retries):
            try:
                return self._query(prompt, temperature=temperature, **kwargs)
            except Exception as err:
                wait = 2 ** retry * 5
                print(f'Error communicating with OpenAI: "{err}"'
                      f' - Retrying in {wait} seconds...')
                time.sleep(wait)
        print(f"Failed after {max_retries} queries - aborting.")
