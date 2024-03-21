FROM python:3.10

RUN pip install gunicorn flask

WORKDIR /app

COPY . /app

CMD [ "gunicorn", "-b :5050", "main:app" ]

EXPOSE 5050
