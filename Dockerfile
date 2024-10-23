# Use amd64 platform
FROM --platform=linux/amd64 python:3.9-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 종속성 파일 복사 및 설치
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# 4. FastAPI 애플리케이션 복사
COPY . .

# 5. 환경변수 로드
ENV PYTHONUNBUFFERED=1

# 6. FastAPI 서버 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
