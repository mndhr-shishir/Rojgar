FROM python:latest

WORKDIR app
COPY . .

RUN pip --no-cache-dir install -r requirements.txt

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8080" ]
