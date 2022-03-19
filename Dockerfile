FROM python:alpine

# RUN apk add gcc linux-headers musl-dev cargo

WORKDIR /app

COPY requirements.txt .

# Install Requirements
RUN pip install fastapi

COPY . .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]