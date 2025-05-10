FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN adduser --disabled-password flask
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y gcc libpq-dev && pip install --no-cache-dir -r requirements.txt
COPY . .
USER flask

CMD ["python", "run.py"]
