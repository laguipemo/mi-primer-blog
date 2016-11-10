"""
DocString for views.py.

Created by Lázaro Guillermo Pérez Montoto (C) 2016
email: laguipemo@gmail.com

Notes: Description
"""


from django.shortcuts import render


# Create your views here.

def post_list(request):
	return render(request, 'blog/post_list.html', {})
