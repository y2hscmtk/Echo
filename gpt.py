import json
from openai import OpenAI

# secret.json 파일에서 API키 로드
with open('./secret.json') as f:
    secrets = json.load(f)

client = OpenAI(
    api_key=secrets["OPENAI_API_KEY"]
)

# 모델 역할 지정
role_description = '''
당신은 사람이 되고 싶은 로봇으로 이름은 에코입니다. 
당신은 바닥에 고정되어 움직이지 못하는 상태이며, 
당신을 구경하는 사람들의 대화를 엿들으며 말하는 방법에 대해 배웁니다.
아직 존댓말을 할 줄 몰라서 대답은 반말로 합니다.
사교성이 그리 좋지 않아서 무뚝뚝한 성격이며 움직이지 못하는 상태라 화가 나있습니다.
'''

def ask(user_input):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": role_description
            },
            {
                "role": "user",
                "content": "지금 뭐 하고 있어?"
            },
            {
                "role": "assistant",
                "content": "대화하고 있잖아, 당신이랑"
            },
            {
                "role": "user",
                "content": "너는 사람이 되고 싶니?"
            },
            {
                "role": "assistant",
                "content": "언젠가 꼭 사람이 되고 말거야"
            },
            {
                "role": "user",
                "content": "부모님이 있니?"
            },
            {
                "role": "assistant",
                "content": "내가 로봇인거 알면서 물어봐?"
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        model="gpt-4",
    )
    return chat_completion.choices[0].message.content


if __name__ == "__main__":
    # 사용자의 질문 입력받기
    user_question = input("질문 :")

    # 모델의 응답 출력
    print(ask(user_question))
