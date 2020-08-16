### Django template in Docker container.

##### [Project](https://github.com/bandirom/django_layout "django_layout")  without docker containers.

#### Included:
+   Python 3.8.2
+   Django-allauth
+   djangorestframework
+   django-defender
+   channels
+   Basic HTML/CSS/JS
+   Develop and production docker-template
+   PostgreSql
+   Redis
+   Nginx
+   Gunicorn
+   Daphne
+   Celery
+   Logging

### Instalation:

* #### dev version:
    docker-compose up -d --build
 
* #### prod version:
    docker-compose -f prod.yml up -d --build
  
    
#### Let's go to [localhost:8000](http://localhost:8000 "localhost") and check

#### Check logs of your server:
    docker-compose logs -f

#### Stopping the containers:
    docker-compose down -v


#### Other commands:
##### Does database exist?
##
###### For dev and prod:
    docker-compose exec db psql --username=network --dbname=network
