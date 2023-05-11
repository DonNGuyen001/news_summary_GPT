import json
import unicodedata
import openai


class ChatGPT:
    def __init__(self, api_key):
        self.openai = openai
        # self.openai.organization ="Vietnam News Agency"
        self.openai.api_key = api_key
        self.messages = []

    def send_request(self, mess, maximum_token=2048, temperature=1.00):
        try:
            self.messages.append({'role': 'user', 'content': mess})
            print(self.messages)
            response = self.openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                temperature=temperature,
                max_tokens=maximum_token,
                messages=self.messages,

            )
            self.messages.append({'role': 'assistant', 'content': response.choices[0].message.content})
            return {'usage': response.usage.total_tokens, 'content': response.choices[0].message.content}
        except Exception as e:
            return {'error': e}

    def send_cmd(self, mess, maximum_token=2048, temperature=1.00):
        try:
            response = self.openai.Completion.create(
                model='text-davinci-003',
                prompt=mess,
                temperature=temperature,
                max_tokens=maximum_token,
            )
            return response["choices"][0]["text"]
        except Exception as e:
            return {'error': e}




