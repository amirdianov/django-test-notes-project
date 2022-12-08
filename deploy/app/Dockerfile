FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN pip install poetry==1.2.2 && poetry config virtualenvs.create false

WORKDIR /app
RUN apt-get update -qq >/dev/null  &&  \
    apt-get install -y libpq-dev python-dev gcc musl-dev  &&  \
    rm -rf /var/lib/apt/lists/* &&  \
    pip install -U pip wheel

RUN git init  # for pre commit hook

#COPY requirements.txt .
#RUN pip install -r requirements.txt
pip install uWSGI==2.0.21
COPY pyproject.toml .
COPY poetry.lock .
COPY .pre-commit-config.yaml .
RUN poetry install && pre-commit install --install-hooks


COPY .. .

RUN pre-commit run -a && python src/manage.py collectstatic --noinput


EXPOSE 8000

CMD python manage.py migrate && \
    uwsgi deploy/app/uwsgi.ini
