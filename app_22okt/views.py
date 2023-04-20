from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound, HttpResponseServerError
from .models import Festo, Kep
from re import search

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

def index(request):
    return render(request, '22okt/index.html')

####################
## 2. feladat
##################

def feladat_2_kerdes(request):
    evszamok = [ festo.szuletett for festo in Festo.objects.all()] + [ festo.meghalt for festo in Festo.objects.all()]
    ettol = min(evszamok)
    eddig = max(evszamok)
    
    template = '22okt/feladat_2_kerdes.html'
    context = {
        'ettol': ettol,
        'eddig': eddig,
    }

    return render(request, template, context)

def feladat_2_valasz(request):
    if request.method!='POST':
        return redirect('/2022/okt/')
    
    try:
        ev = int(request.POST['ev'])
    except: 
        return HttpResponseServerError('az év nem szám.')
    
    festok = [festo for festo in Festo.objects.all() if festo.szuletett <= ev and ev <= festo.meghalt]
    
    template = '22okt/feladat_2_valasz.html'
    context = {
        'ev': ev,
        'festok': festok,
    }
    return render(request, template, context)

####################
## 3. feladat
##################

def feladat_3_kerdes(request):
    technikak = {kep.technika for kep in Kep.objects.all()}
    
    template = '22okt/feladat_3_kerdes.html'
    context = {
        'technikak':technikak,
    }
    return render(request, template, context)

def feladat_3_valasz(request):
    if request.method!='POST':
        return redirect('/2022/okt/')

    a_technika = request.POST['technika']
    anyagok = {kep.anyag for kep in Kep.objects.filter(technika=a_technika)}

    template = '22okt/feladat_3_valasz.html'
    context = {
        'anyagok':anyagok,
    }
    return render(request, template, context)

####################
## 4. feladat
##################


def feladat_4_kerdes(request):    
    return render(request, '22okt/feladat_4_kerdes.html')

def feladat_4_valasz(request):
    if request.method!='POST':
        return redirect('/2022/okt/')
    
    karaktersorozat = request.POST['karaktersorozat']    
    kepek = [kep for kep in Kep.objects.all() if search(r'^.*' + karaktersorozat + r'.*$', kep.cim)]
    
    template = '22okt/feladat_4_valasz.html'
    context = {
        'karaktersorozat': karaktersorozat,
        'kepek': kepek,
    }
    return render(request, template, context)

####################
## 5. feladat
##################

def feladat_5_valasz(request):
    template = '22okt/feladat_5_valasz.html'    
    maxmagassag = max(kep.magas for kep in Kep.objects.all())
    legmagasabb_kep = Kep.objects.get(magas=maxmagassag)
    context = {
        'legmagasabb_kep': legmagasabb_kep,
    }
    return render(request, template, context)

####################
## 6. feladat
##################

def feladat_6_valasz(request):
    sorok = sorted(Kep.melyik_evben_hany_kep_keszult(), key=lambda sor: sor['ev'])
    
    template = '22okt/feladat_6_valasz.html'
    context = {
        'sorok': sorok,
    }
    
    return render(request, template, context)