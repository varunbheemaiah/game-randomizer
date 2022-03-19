FROM python:alpine

RUN apk add gcc

WORKDIR /app

COPY requirements.txt .

# Install Requirements
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn"  , "app:app"]