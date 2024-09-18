FROM python:3.10-slim-buster

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

EXPOSE 8501
# hei
CMD ["streamlit","run","app.py"]