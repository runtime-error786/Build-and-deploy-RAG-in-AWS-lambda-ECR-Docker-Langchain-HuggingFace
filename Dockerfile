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


FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy your app and requirements.txt
COPY . /app
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install streamlit if it's not in requirements.txt
RUN pip install streamlit

# Expose the default streamlit port
EXPOSE 8501

# Command to run your streamlit app
CMD ["streamlit", "run", "your_app.py", "--server.port", "8080"]
