"""
DocString for admin.py.

Created by Lázaro Guillermo Pérez Montoto (C) 2016
email: laguipemo@gmail.com

Notes: Description
"""


from django.contrib import admin
from .models import Post

# Register your models here.

admin.site.register(Post)
