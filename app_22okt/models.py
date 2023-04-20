from django.db import models

# Create your models here.

class Festo(models.Model):

    azon = models.IntegerField()
    nev = models.CharField(max_length=255)
    szuletett = models.IntegerField()
    meghalt = models.IntegerField()

    class Meta:
        verbose_name = "Festő"
        verbose_name_plural = "Festők"

    def __str__(self): # legyen rendesen kidolgozott __str__!
        return f'{self.nev} ({self.szuletett}-{self.meghalt})'

    def import_from_tsv(szoveg):
        szoveg = szoveg.strip()
        sorok = [sor.strip() for sor in szoveg.split('\n')] # \r is maradhat ott

        db = 0
        for i, sor in enumerate(sorok):
            if i==0:
                continue
            sortomb = sor.split('\t')

            for oszlop in [0, 2, 3]:
                if not sortomb[oszlop].isdigit():
                    error = f'A(z) {i}. sor {oszlop + 1}. oszlopában ez nem szám: {sortomb[oszlop]}'
                    print([sortomb[oszlop]])
                    return db, error

            festo, is_created = Festo.objects.get_or_create(
                azon = int(sortomb[0]),
                nev = sortomb[1],
                szuletett = int(sortomb[2]),
                meghalt = int(sortomb[3]),
            )

            if is_created:
                db+=1
        
        error = None
        return db, error



class Kep(models.Model):

    leltar = models.CharField(max_length=255)
    festo = models.ForeignKey(Festo, on_delete=models.CASCADE) # így hivjuk, ne fazonnak! Azt majd beolvasáskor illesztjük!
    cim = models.CharField(max_length=255)
    keszult = models.IntegerField()
    anyag = models.CharField(max_length=255)
    technika = models.CharField(max_length=255)
    szeles = models.FloatField()
    magas = models.FloatField()
    

    class Meta:
        verbose_name = "Kép"
        verbose_name_plural = "Képek"

    def __str__(self): # legyen rendesen kidolgozott __str__!
        return f'{self.festo}: {self.cim} ({self.keszult}). {self.anyag}, {self.technika}, {self.szeles}x{self.magas}'


    def import_from_tsv(szoveg):
        szoveg = szoveg.strip()
        sorok = [sor.strip() for sor in szoveg.split('\n')] # \r is maradhat ott

        db = 0
        for i, sor in enumerate(sorok):
            if i==0:
                continue
            sortomb = sor.split('\t')

            for oszlop in [1, 3]:
                try:
                    sortomb[oszlop] = int(sortomb[oszlop])
                except: 
                    error = f'A(z) {i}. sor {oszlop + 1}. oszlopában ez nem int: {sortomb[oszlop]}'
                    return db, error

            for oszlop in [6, 7]:
                try:
                    sortomb[oszlop] = float(sortomb[oszlop].replace(',', '.'))
                except: 
                    error = f'A(z) {i}. sor {oszlop + 1}. oszlopában ez nem float: {sortomb[oszlop]}'
                    return db, error

            fazon = int(sortomb[1]) # tehát nem tulajdonság, hanem arra használjuk, hogy ez alapján keressük ki a másikból!
            a_festo = Festo.objects.filter(azon=fazon).first() # azért nem get, mert ez None, ha nem talál.
            if a_festo == None:
                error = f'A(z) {i}. sorban a {fazon} azonosítóhoz nem található festő a festők táblájában. Biztos, hogy fel lett töltve a festők táblája?'
                return db, error


            festo, is_created = Kep.objects.get_or_create(
                leltar = sortomb[0],
                festo = a_festo, # az objectet magát rakjuk ide a foreign keynek!
                cim = sortomb[2],
                keszult = sortomb[3],
                anyag = sortomb[4],
                technika = sortomb[5],
                szeles = sortomb[6],
                magas = sortomb[7],
            )

            if is_created:
                db+=1
        
        error = None
        return db, error

    def melyik_evben_hany_kep_keszult():
        szotar = {}
        for kep in Kep.objects.all():
            if kep.keszult in szotar.keys():
                szotar[kep.keszult] += 1
            else:
                szotar[kep.keszult] = 1
        
        return [{'ev': ev, 'db': szotar[ev]} for ev in szotar.keys()] 
        
    
    
