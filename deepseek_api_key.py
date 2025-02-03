from openai import OpenAI

import os

from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

client = OpenAI(api_key=os.environ["DeepSeek_API_Key"], base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)