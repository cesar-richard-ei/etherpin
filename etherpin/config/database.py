import dj_database_url
import environ

env = environ.Env(
    ETHERPIN_DJANGO_SECRET=(str, "whatever"),
    ETHERPIN_DB_DEFAULT=(str, ""),
)

if env("ETHERPIN_DJANGO_SECRET") != "whatever":
    DATABASES = {"default": dj_database_url.parse(env("ETHERPIN_DB_DEFAULT"))}
    DATABASES["default"]["ENGINE"] = "django.db.backends.postgresql"
