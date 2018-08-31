from django.core.handlers.wsgi import WSGIHandler

from main.wsgi import application


def test_wsgi():
    assert type(application) == WSGIHandler
