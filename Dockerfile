FROM python:3.11-slim

RUN mkdir app

WORKDIR app/

COPY req.txt /app/

RUN python -m pip install -r req.txt

COPY . /app/

CMD python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py collectstatic --no-input \
    && python manage.py runserver