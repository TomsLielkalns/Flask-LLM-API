FROM python:3.13-alpine

WORKDIR /app
COPY . /app/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]