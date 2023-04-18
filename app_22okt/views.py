from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound, HttpResponseServerError
from .models import Festo, Kep

# a views.py-ban az áll, ahogy a szerver kommunikál a felhasználóval. 
# fontos, hogy a programozási részletek nem itt vannak. 
# itt most a models.py-ba vannak száműzve, mert úgyis ott vannak a modellek, amikkel dolgoznak. (Egyébként ez sem az igazi.)

def feltolt_get(request, tabla):
    if tabla not in ['festo', 'kep']:
        return HttpResponseNotFound('Ilyen tábla nincs')
        
    template = '22okt/feltolt.html'
    context = {
        'cim': tabla,
        'tabla': tabla,
    }
    return render(request, template, context)

def feltolt_post(request, tabla):
    # Hibakezelés if-returnökkel!
    if request.method!="POST":
        return HttpResponseForbidden('eltévedtél')
    if 'szoveg' not in request.POST.keys():
        return HttpResponseForbidden('ne mókolj a posttal')
    if tabla not in ['festo', 'kep']:
        return HttpResponseNotFound('Ilyen tábla nincs')

    # a feladatkiosztás és a válasz logikája. A technikai részletek ne a views.py-ban legyenek!
    if tabla == 'festo':
        db, error = Festo.import_from_tsv(request.POST['szoveg'])
        if error!=None:
            return HttpResponseServerError(f'{db} db sort fel tudtunk dolgozni, de: '+ error)
        ossz = Festo.objects.all().count()
    elif tabla == 'kep':
        db, error = Kep.import_from_tsv(request.POST['szoveg'])    
        if error!=None:
            return HttpResponseServerError(f'{db} db sort fel tudtunk dolgozni, de: '+ error)
        ossz = Kep.objects.all().count()
    return HttpResponse(f'Sikerült a feltöltés a {tabla} táblába, {db} új adat jött létre. A többi már létezett korábban is. Így most {ossz} db adat van összesen.')
