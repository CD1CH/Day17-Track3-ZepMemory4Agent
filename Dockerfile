FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/workspace

WORKDIR /workspace

COPY requirements.txt /tmp/requirements.txt
RUN pip install --default-timeout=1000 --retries 10 --upgrade pip && \
    pip install --default-timeout=1000 --retries 10 -r /tmp/requirements.txt

COPY . /workspace

CMD ["sleep", "infinity"]
