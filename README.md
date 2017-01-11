# username_validator is not working

## Goal

Replace User's username validator from django.auth.models.

## Document

The code follows [username_validator](https://docs.djangoproject.com/en/1.10/ref/contrib/auth/#django.contrib.auth.models.User.username_validator)
description.

## Problem

`username_validator` is still referred to original validator ([UnicodeUsernameValidator](https://github.com/django/django/blob/master/django/contrib/auth/validators.py)).

## Way I did

```
(venv) $ pip install -r requirements.txt
(venv) $ python manage.py migrate
(venv) $ python manage.py createsuperuser 
(venv) $ python manage.py runserver
```

Then access to [admin backend](http://localhost:8000/admin), create a user.

## Reason?

Is `username_validator` already assigned before hit the new validator? check [django.contrib.auth.models](https://github.com/django/django/blob/master/django/contrib/auth/models.py#L313).

