from fastapi import FastAPI
from pydantic import BaseModel
import openai
from dotenv import load_dotenv
import os

# .env 파일에서 API 키 로드
load_dotenv()

# GPT-4o-mini API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# FastAPI 애플리케이션 초기화
app = FastAPI()


# 데이터 모델 정의
class TextInput(BaseModel):
    text: str


# 광고/스팸 분류 함수
def classify_text(text):
    prompt = f"다음 text가 광고나 스팸메시지인 것 같으면 '광고' or 그냥 일반적인 text라면 '일반': {text}"
    response = openai.Completion.create(
        engine="gpt-4o-mini",
        temperature=0,
        prompt=prompt,
        max_tokens=10
    )
    return response.choices[0].text.strip()


# 요약 함수
def summarize_text(text):
    prompt = f"다음 text에 간략하게 두 개의 문장으로 요약해줘. : {text}"
    response = openai.Completion.create(
        engine="gpt-4o-mini",
        prompt=prompt,
        temperature=0,
        max_tokens=50
    )
    return response.choices[0].text.strip()


# API 엔드포인트: 텍스트 분류 및 요약
@app.post("/classify-and-summarize")
def classify_and_summarize(input_data: TextInput):
    # 텍스트 분류
    classification = classify_text(input_data.text)

    # 텍스트 요약
    summary = summarize_text(input_data.text)

    return {"classification": classification, "summary": summary}
