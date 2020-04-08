### Init django
    pip install -r requirements.txt
    django-admin startproject src .
    python manage.py startapp app

```
 # settings.py:

 SITE_ID = 1
 LOGIN_REDIRECT_URL = '/'

 INSTALLED_APPS = [
    'django.contrib.sites',
    'django_extensions',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'app',
]
```

    python manage.py migrate
    python manage.py createsuperuser

    python manage.py runserver_plus --cert-file cert.crt


#### Create FB and Google providers for Oauth2.0
```
    https://127.0.0.1:8000/admin/socialaccount
    
```