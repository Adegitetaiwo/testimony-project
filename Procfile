web: gunicorn testimony.wsgi —-log-file -
web: python testimony/manage.py collectstatic --noinput; gunicorn --pythonpath testimony testimony.wsgi