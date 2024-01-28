import json
from openai import OpenAI

# secret.json 파일에서 API키 로드
with open('secret.json') as f:
    secrets = json.load(f)

client = OpenAI(
    api_key=secrets["OPENAI_API_KEY"]
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)