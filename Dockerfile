# syntax=docker/dockerfile:1
FROM python:3.11-slim-bullseye as app
WORKDIR /app

RUN apt-get update \
  && apt-get install -y --no-install-recommends build-essential curl libpq-dev \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean \
  && useradd --create-home python \
  && chown python:python -R /app \
  && mkdir /static \
  && chown python:python -R /static

USER python

# Copy local django/ contents to container /app (WORKDIR)
COPY --chown=python:python . .

ENV DJANGO_SETTINGS_MODULE="project.settings" \
    PYTHONUNBUFFERED="true" \
    PYTHONPATH="/app" \
    PATH="${PATH}:/home/python/.local/bin"

COPY requirements.txt /app/
COPY requirements-dev.txt /app/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements-dev.txt
COPY . /app/
RUN pip install -e .
RUN django-admin collectstatic --no-input;

ENTRYPOINT [ "/app/docker/entrypoint.sh" ]

EXPOSE 8000

CMD ["python -m gunicorn", "-c", "python:project.gunicorn", "project.wsgi"]