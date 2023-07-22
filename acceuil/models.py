from django.db import models


# Create your models here.

class AcceuilContact(models.Model):
    nom = models.CharField(max_length=50, null=True, )
    email = models.EmailField(max_length=50)
    telephone = models.FloatField(max_length=50)
    detail = models.TextField(max_length=500)

    class Meta:
        verbose_name = ("AcceuilContact")
        verbose_name_plural = ("AcceuilContact")

    def __str__(self):
        return self.nom
