FROM python:alpine

RUN apk add gcc

RUN apk add linux-headers

RUN apk add musl-dev

WORKDIR /app

COPY requirements.txt .

# Install Requirements
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn"  , "app:app"]