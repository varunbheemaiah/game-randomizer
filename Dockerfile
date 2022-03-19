FROM python:alpine

WORKDIR /app

COPY requirements.txt .

# Install Requirements
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn"  , "app:app"]