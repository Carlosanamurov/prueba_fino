# Stage 1: Builder
FROM python:3.9-slim as builder

WORKDIR /app
COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.9-slim

WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
       
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Dependiendo del entorno
ARG ENVIRONMENT
RUN if [ "$ENVIRONMENT" = "production" ]; then \
        pip install gunicorn && \
        chmod +x /app/docker-entrypoint.sh; \
    fi

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]