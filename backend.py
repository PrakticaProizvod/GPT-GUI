import requests
import openai
import os
from dotenv import load_dotenv

load_dotenv()


def get_response_text(message):
    client = openai.OpenAI(
        api_key=f"{os.getenv('key')}",
        base_url="https://api.proxyapi.ru/openai/v1",
    )

    model = "gpt-4o"

    chat_completion = client.chat.completions.create(
        model=model, messages=[{"role": "user", "content": message}]
    )

    return chat_completion.choices[0].message.content


def get_response_photo(message):
    client = openai.OpenAI(
        api_key=f"{os.getenv('key')}",
        base_url="https://api.proxyapi.ru/openai/v1",
    )

    response = client.images.generate(
        model="dall-e-3",
        prompt=f"{message}",
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url

    response = requests.get(image_url)

    with open("image.png", "wb") as f:
        f.write(response.content)

    print("Image saved to image.png")