# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_APP=pond5.app:create_app
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
ENV ENV=pond5.ext.config.DevConfig
ENV ENV_TEST=pond5.ext.config.TestingConfig
ENV DATABASE_URL=sqlite:///development.db


COPY requirements.txt requirements.txt
COPY requirements-dev.txt requirements-dev.txt
COPY setup.py setup.py
RUN pip install -e .[dev]

EXPOSE 5000
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]