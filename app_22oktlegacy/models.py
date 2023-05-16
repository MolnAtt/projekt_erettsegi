from django.db import models

# Create your models here.

class Kerulet(models.Model):

    szam = models.CharField(max_length=50)
    nev = models.CharField(max_length=100, blank=True, null=True)
    lakossag = models.IntegerField()
    terulet = models.FloatField()

    class Meta:
        verbose_name = "Kerület"
        verbose_name_plural = "Kerületek"

    def __str__(self):
        return self.szam + "(" + (self.nev if self.nev!=None else "") + ")"
    
    def feltolt(inputcsv):
        sorok = [ sor.strip() for sor in inputcsv.strip().split('\n')]
        darab = 0

        for i, sor in enumerate(sorok[1:]):
            sortomb = sor.split('\t')

            if len(sortomb)<4:
                return (darab, f'a(z) {i+1}. rekordban kevés a tabulátorok száma!')
            
            try:
                a_lakossag = int(sortomb[2])
            except:
                return (darab, f'a(z) {i+1}. rekordban a harmadik mezőben nem egész szám található!')

            try:
                a_terulet = float(sortomb[3].replace(',','.'))
            except:
                return (darab, f'a(z) {i+1}. rekordban a harmadik mezőben nem tizedestört található!')

            _, is_created = Kerulet.objects.get_or_create(
                szam = sortomb[0],
                nev = sortomb[1],
                lakossag = a_lakossag,
                terulet = a_terulet,
            )

            if  is_created:
                darab += 1

        return (darab, None)
        # errorokat még dolgozzuk ki hétfőn!!!! 
        # Visszajelzés, hogy mi sikerült, mennyit sikerült, stb.
            

class Varosresz(models.Model):

    azon = models.IntegerField()
    nev = models.CharField(max_length=100, blank=True, null=True)
    lakossag = models.IntegerField(blank=True, null=True)
    kerulet = models.ManyToManyField(Kerulet, blank=True)

    class Meta:
        verbose_name = "Városrész"
        verbose_name_plural = "Városrészek"

    def feltolt(inputcsv):
        sorok = [ sor for sor in inputcsv.replace('\r\n', '\n').strip().split('\n')]
        darab = 0

        for i, sor in enumerate(sorok[1:]):
            sortomb = sor.split('\t')

            ## holnap innen folytatjuk
            print(f'{i}. sor következik: {sor}')
            print(sortomb)

            if len(sortomb)<2:
                return (darab, f'a(z) {i+1}. rekordban kevés a tabulátorok száma!')
            
            try:
                az_azon = int(sortomb[0])
            except:
                return (darab, f'a(z) {i+1}. rekordban az első mezőben nem egész szám található!')


            try:
                a_lakossag = int(sortomb[2]) if sortomb[2]!='' else None
            except:
                return (darab, f'a(z) {i+1}. rekordban a harmadik mezőben nem egész szám található!')


            _, is_created = Varosresz.objects.get_or_create(
                azon = az_azon,
                nev = sortomb[1],
                lakossag = a_lakossag,
            )

            if  is_created:
                darab += 1

        return (darab, None)
        # errorokat még dolgozzuk ki hétfőn!!!! 
        # Visszajelzés, hogy mi sikerült, mennyit sikerült, stb.
            

    def feltolt_kapcsolat(inputcsv):
        sorok = [ sor for sor in inputcsv.replace('\r\n', '\n').strip().split('\n')]
        darab = 0

        for i, sor in enumerate(sorok[1:]):
            sortomb = sor.split('\t')

            ## holnap innen folytatjuk
            print(f'{i}. sor következik: {sor}')
            print(sortomb)

            if len(sortomb)<3:
                return (darab, f'a(z) {i+1}. rekordban kevés a tabulátorok száma!')
            
            try:
                melyik_varosresz_int = int(sortomb[1])
            except:
                return (darab, f'a(z) {i+1}. rekordban a második mezőben nem egész szám található!')


            melyik_kerulet_str = sortomb[2] # "XII."

            melyik_varosresz = Varosresz.objects.get(azon = melyik_varosresz_int)
            melyik_kerulet = Kerulet.objects.get(szam = melyik_kerulet_str)

            melyik_varosresz.kerulet.add(melyik_kerulet) # a ".kerület" tulajdonság nem más, mint azon kerületek halmaza, amelyekkel össze van kapcsolva!
            darab+=1

            print(melyik_kerulet, melyik_varosresz)

        return (darab, None)
        # errorokat még dolgozzuk ki hétfőn!!!! 
        # Visszajelzés, hogy mi sikerült, mennyit sikerült, stb.
            
    def __str__(self):
        return f'{self.nev} ({self.azon})'


