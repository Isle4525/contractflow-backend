web: python manage.py check && python manage.py collectstatic --noinput && gunicorn config.wsgi --bind 0.0.0.0:$PORT --log-level debug --preload
release: python manage.py migrate --noinput
