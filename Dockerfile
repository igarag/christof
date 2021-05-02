FROM python:3.8-slim

WORKDIR /app/app

COPY ./requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r ./requirements.txt

COPY ./app /app/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]