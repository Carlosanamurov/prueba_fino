FROM python:3.9
WORKDIR /opt/app
COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir --default-timeout=100 -r requirements.txt
COPY . .
ENV PYTHONPATH=/opt/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]