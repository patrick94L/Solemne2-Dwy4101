from django.db import models

# Create your models here.
class Plan(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    minutes = models.IntegerField(default=0)
    internet = models.IntegerField(default=0)

    def str(self):
        return self.title