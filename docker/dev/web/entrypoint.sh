#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

cd /usr/src/web

python manage.py makemigrations
python manage.py migrate
#python manage.py collectstatic --no-input
python manage.py runserver 0.0.0.0:8000
#daphne -b 0.0.0.0 -p 8000 src.asgi:application
exec "$@"

