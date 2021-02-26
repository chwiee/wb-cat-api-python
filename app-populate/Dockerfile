FROM python:3.5-alpine
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
