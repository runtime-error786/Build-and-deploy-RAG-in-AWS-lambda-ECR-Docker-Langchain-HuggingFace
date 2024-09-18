FROM python:3.11.3-slim-buster

WORKDIR /app

# Install system dependencies if required
RUN apt-get update && apt-get install -y \
    gcc \
    libssl-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
