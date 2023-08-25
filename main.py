from fastapi import FastAPI
from pydantic import BaseModel
import openai

import gpt_api_key

app = FastAPI()

# OpenAI API 키 설정
openai.api_key = gpt_api_key.OPENAI_API_KEY  # 여기에 실제 API 키를 입력하시거나 외부에서 불러오십시오.


class Data(BaseModel):
    content: str


@app.post("/generate_fitness_report1/")
async def generate_report(data: Data):
    print(data)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a health trainer"
            },
            {
                "role": "user",
                "content": data.content
            },
            {
                "role": "assistant",
                "content": ""
            }
        ],
        temperature=1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    ai_message = response.choices[0].message['content']
    return {"ai_message": ai_message}


# FastAPI 앱 실행
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
