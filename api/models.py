from django.db import models

# Create your models here.
class Client(models.Model):
    username = models.CharField(max_length=50)
    is_active  = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.username}"