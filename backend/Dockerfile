FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]

HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD curl http://localhost:5000/healthz || exit
