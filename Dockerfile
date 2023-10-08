FROM python:3.11-slim-bookworm AS builder
LABEL org.opencontainers.image.authors="Cesar Richard <cesar@crichard.fr>"

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PATH="/home/etherpin/.local/bin:${PATH}"

ENV BUILD_DEPS="build-essential"

# Setup working directory
RUN mkdir -p /srv /home/etherpin/.ssh /static
WORKDIR /srv

# Setup user
RUN groupadd -r etherpin && useradd -r -g etherpin etherpin

# Install tmate for shells
RUN apt-get update && apt-get dist-upgrade -y && apt-get install --no-install-recommends -y ${BUILD_DEPS}

RUN chown etherpin:etherpin -R /home/etherpin /srv

FROM builder AS dependencies

# Install uwsgi
RUN pip install --no-cache-dir uwsgi

# Install etherpin requirements (doing this before copying code improves caching)
ADD requirements.txt /srv/
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get purge -y ${BUILD_DEPS} && apt-get autoremove -y && apt-get clean -y && rm -r /var/lib/apt/lists/*
# Uwsgi runs on port 8000
EXPOSE 8000
# Add code
ADD . /srv/
# Switch to unprivileged user
USER etherpin

FROM dependencies AS front_builder
# Collect static files
RUN ETHERPIN_DJANGO_SECRET=whatever python manage.py collectstatic --noinput --clear

FROM front_builder AS development
RUN pip install --no-cache-dir -r requirements-dev.txt
# Run uwsgi
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM front_builder AS final
# Run uwsgi
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM dependencies AS migrator
# Run migrations
CMD ["python", "manage.py", "migrate", "--noinput"]
