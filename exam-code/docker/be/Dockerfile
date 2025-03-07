# Dockerfile for Backend Service
FROM python:3.12-slim
WORKDIR /src
COPY requirements.txt /src/
RUN pip install --no-cache-dir -r requirements.txt
COPY /src /src/
CMD ["python", "main.py"]
EXPOSE 5001