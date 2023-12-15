FROM python:3.11-slim

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

RUN mkdir app

WORKDIR app/

COPY req.txt /app/

RUN python -m pip install -r req.txt

COPY . /app/

CMD python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py collectstatic --no-input \
    && python manage.py runserver 0.0.0.0:8000
