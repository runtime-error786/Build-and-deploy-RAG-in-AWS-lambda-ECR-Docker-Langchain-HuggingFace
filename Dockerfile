FROM python:3.11.3-slim-buster

WORKDIR /app

COPY . /app/

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libssl-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD ["streamlit", "run", "app.py"]
