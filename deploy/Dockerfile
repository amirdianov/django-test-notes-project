FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app
RUN apt-get update -qq >/dev/null  &&  \
    apt-get install -y libpq-dev python-dev gcc musl-dev  &&  \
    rm -rf /var/lib/apt/lists/* &&  \
    pip install -U pip wheel

COPY requirements.txt .
RUN pip install -r requirements.txt


COPY . .

EXPOSE 8000

CMD python manage.py migrate && \
    python manage.py runserver 0.0.0.0:8000
