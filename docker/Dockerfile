FROM python:3.11-slim-bookworm AS builder
LABEL org.opencontainers.image.authors="Cesar Richard <cesar@crichard.fr>"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PATH="/home/etherpin/.local/bin:${PATH}"

ENV BUILD_DEPS="build-essential curl"

# Setup working directory
RUN mkdir -p /srv /home/etherpin/.ssh /static
WORKDIR /srv

# Setup user
RUN groupadd -r etherpin && useradd -r -g etherpin etherpin

# Install tmate for shells
RUN apt-get update && apt-get dist-upgrade -y && apt-get install --no-install-recommends -y ${BUILD_DEPS}
RUN curl -1sLf \
    'https://dl.cloudsmith.io/public/infisical/infisical-cli/setup.deb.sh' |  bash
RUN apt-get install --no-install-recommends -y infisical
RUN chown etherpin:etherpin -R /home/etherpin /srv

FROM builder AS dependencies
# Install uwsgi
RUN pip install --no-cache-dir uwsgi
# Install etherpin requirements (doing this before copying code improves caching)
ADD requirements.txt /srv/
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get purge -y ${BUILD_DEPS} && apt-get autoremove -y && apt-get clean -y && rm -r /var/lib/apt/lists/*
RUN unset BUILD_DEPS
# Uwsgi runs on port 8000
EXPOSE 8000

FROM dependencies AS front_builder
ADD . /srv/
# Collect static files
RUN ETHERPIN_DJANGO_SECRET=whatever python manage.py collectstatic --noinput --clear
USER etherpin

FROM dependencies AS development
ADD requirements-dev.txt /srv/
RUN pip install --no-cache-dir -r requirements-dev.txt
ADD . /srv/
RUN ETHERPIN_DJANGO_SECRET=whatever python manage.py collectstatic --noinput --clear
USER etherpin
# Run uwsgi
ENV XDEBUG_PORT 3000
CMD ["infisical", "run", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM front_builder AS final
# Run uwsgi
CMD ["infisical", "run", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM dependencies AS migrator
ENV XDEBUG_PORT 3000
ADD . /srv/
# Run migrations
CMD ["infisical", "run", "--path", "/database", "--", "python", "manage.py", "migrate", "--noinput"]
