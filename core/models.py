from django.db import models

class Person(models.Model):
    POSITION_CHOICES = (
        ('President', 'President'),
        ('Vice President', 'Vice President'),
        ('General Secretary', 'Joint Secretary'),
        ('Treasurer', 'Treasurer'),
        ('Convener', 'Convener'),
        ('Head of Coorporate communication', 'Head of Coorporate communication'),
        ('Head of Operations','Head of Operations'),
        ('Technical Head','Technical Head'),
        ('Baja Coordinator','Baja Coordinator'),
        ('Creative Head','Creative Head'),
        ('Publicity Head','Publicity Head'),
        ('Webd Head', 'Webd Head'),
        ('Head Ath', 'Head Ath'),
        ('Event Head','Event Head'),
        ('WorkShop Head','WorkShop Head'),        
    )

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, choices=POSITION_CHOICES)
    image = models.ImageField(upload_to='person_images/')
    linkedin = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    
    def __str__(self):
        return self.name

