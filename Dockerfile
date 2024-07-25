FROM python:3.10-slim

WORKDIR /ai_stylist

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY /app /ai_stylist/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
