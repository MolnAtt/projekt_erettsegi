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
    
class Varosresz(models.Model):

    azon = models.IntegerField()
    nev = models.CharField(max_length=100, blank=True, null=True)
    lakossag = models.IntegerField(blank=True, null=True)
    kerulet = models.ManyToManyField(Kerulet, blank=True)

    class Meta:
        verbose_name = "Városrész"
        verbose_name_plural = "Városrészek"

    def __str__(self):
        return f'{self.nev} ({self.azon})'


