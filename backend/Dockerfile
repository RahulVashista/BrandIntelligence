FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml ./
RUN pip install --no-cache-dir -U pip && pip install --no-cache-dir . pytest
COPY app ./app
COPY tests ./tests
