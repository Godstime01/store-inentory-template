from django.db import models

# Create your models here.
class Item(models.Model):
          name = models.CharField(max_length=200)
          price = models.DecimalField(max_digits=3, decimal_places=2)
          quantity = models.IntegerField()
          expiry_date = models.DateField()
          date_added = models.DateTimeField(auto_now_add=True)
          
          def __str__(self): self.name