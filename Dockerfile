FROM python:3.8

EXPOSE 8000

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt --no-cache

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:api"]