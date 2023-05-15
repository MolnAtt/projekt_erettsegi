from django.shortcuts import render
from .models import Kerulet, Varosresz
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound, HttpResponseServerError, HttpResponseBadRequest, HttpResponseNotAllowed

# Create your views here.

def index(request):
    template = 'index.html'
    context = {}
    return render(request, template, context)

def kerulet_feltolt_urlap(request):
    template = 'feltolt.html'
    context = {}
    return render(request, template, context)

def feltoltes_kerulet(request):
    if request.method!='POST':
        return HttpResponseNotAllowed('Nem gombra nyomva jutottál ide!')
    

    Kerulet.feltolt(request.POST['inputcsv'])


    template = 'valasz.html'
    context = {}
    return render(request, template, context)

