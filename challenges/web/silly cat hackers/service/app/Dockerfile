FROM python:3.11-slim-buster

RUN pip install flask
COPY app.py .
COPY ./static ./static/
COPY ./templates ./templates/

EXPOSE 1337
CMD ["python", "app.py"]
