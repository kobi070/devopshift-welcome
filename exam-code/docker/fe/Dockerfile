# Dockerfile for Frontend Service
FROM python:3.12-slim
WORKDIR /src
COPY requirements.txt /src/
RUN pip install --no-cache-dir -r requirements.txt
COPY /src /src/
EXPOSE 5002
CMD ["python", "main.py"]

