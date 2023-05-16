from django.shortcuts import render
from .models import Kerulet, Varosresz
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound, HttpResponseServerError, HttpResponseBadRequest, HttpResponseNotAllowed

# Create your views here.

def index(request):
    template = 'index.html'
    context = {}
    return render(request, template, context)

def feltolt_urlap(request):
    template = 'feltolt.html'
    context = {}
    return render(request, template, context)

def feltoltes_kerulet(request):
    if request.method!='POST':
        return HttpResponseNotAllowed('Nem gombra nyomva jutottál ide!')
    
    darab, error = Kerulet.feltolt(request.POST['inputcsv'])

    if error!=None:
        return HttpResponseServerError(f'Hát sikerült {darab} db rekordot felvinni, aztán történt egy kis probléma... '+ error)

    return HttpResponse(f'Sikerült!! {darab} db új elem jött létre az adatbázisban, így most összesen {Kerulet.objects.all().count()} db rekord van az adatbázisban.')



# def feltoltes(tabla:str, request):
    # if tabla not in ['varosresz', 'kapcsolat', 'kerulet']:
    #     pass
    #     #hibüzenet
    
    # if tabla == 'varosresz':
    #     klassz = Varosresz
    # if tabla == 'varosresz':
    #     klassz = Kerulet
    # # if tabla == 'varosresz':
    #     # klassz = Kapcsolat
    

def feltoltes_varosresz(request):
    if request.method!='POST':
        return HttpResponseNotAllowed('Nem gombra nyomva jutottál ide!')
    
    darab, error = Varosresz.feltolt(request.POST['inputcsv'])

    if error!=None:
        return HttpResponseServerError(f'Hát sikerült {darab} db rekordot felvinni, aztán történt egy kis probléma... '+ error)

    return HttpResponse(f'Sikerült!! {darab} db új elem jött létre az adatbázisban, így most összesen {Varosresz.objects.all().count()} db rekord van az adatbázisban.')


    # template = 'valasz.html'
    # context = {}
    # return render(request, template, context)


def feltoltes_kapcsolat(request):
    if request.method!='POST':
        return HttpResponseNotAllowed('Nem gombra nyomva jutottál ide!')
    
    darab, error = Varosresz.feltolt_kapcsolat(request.POST['inputcsv'])

    if error!=None:
        return HttpResponseServerError(f'Hát sikerült {darab} db kapcsolatot létrehozni, de aztán történt egy kis probléma... '+ error)

    return HttpResponse(f'Sikerült!! {darab} db új kapcsolat jött létre az adatbázisban.')


