"""
DocString for urls.py.

Created by Lázaro Guillermo Pérez Montoto (C) 2016
email: laguipemo@gmail.com

Notes: Description
"""


from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
