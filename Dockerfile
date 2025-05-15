FROM python:3.9
WORKDIR /opt/app/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /opt/app
ENV PYTHONPATH=/opt/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]