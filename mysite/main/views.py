from django.shortcuts import render
from django.http import HttpResponse
from httplib2 import Http

# Create your views here.

def index(response):
    return HttpResponse("<strong>Object Of Type Closure!</strong>")

def v1(response):
    return HttpResponse("<h1>View 1!</h1>")

def another(response):
    return HttpResponse("<em>Anoda view here broda!</em>")

def lastone(response):
    content = """
    <p>
    Some sweet things:
        <ul>
            <li>Cheese</li>
            <li>Milk</li>
        </ul>
    </p>
    """
    return HttpResponse(content)