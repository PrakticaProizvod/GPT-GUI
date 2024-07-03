import openai
import os

from dotenv import load_dotenv

load_dotenv()


def get_response_text(message):
    client = openai.OpenAI(
        api_key=f"{os.getenv('key')}",
        base_url="https://api.proxyapi.ru/openai/v1",
    )

    chat_completion = client.chat.completions.create(
        model="gpt-4o", messages=[{"role": "user", "content": message}]
    )

    return chat_completion.choices[0].message.content