web: python manage.py collectstatic --noinput && gunicorn config.wsgi --bind 0.0.0.0:$PORT --log-level debug
release: python manage.py migrate --noinput
