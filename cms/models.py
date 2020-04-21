from django.db import models


# Create your models here.

class Portfolio(models.Model):
    company_name = models.CharField(max_length=50)
    date = models.DateField()
    featured_image = models.ImageField(upload_to='images/portfolio/')

    def __str__(self):
        return self.company_name
    
    class Meta:
        ordering = ['date']

class ClientTestimony(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
