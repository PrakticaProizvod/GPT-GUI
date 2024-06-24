import openai
from api import key


def get_response(message):
    client = openai.OpenAI(
        api_key=f"{key}",
        base_url="https://api.proxyapi.ru/openai/v1",
    )

    chat_completion = client.chat.completions.create(
        model="gpt-4o", messages=[{"role": "user", "content": message}]
    )

    return chat_completion.choices[0].message.content