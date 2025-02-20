FROM python:3.11

COPY . .

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["uvicorn",  "main:app", "--reload"]