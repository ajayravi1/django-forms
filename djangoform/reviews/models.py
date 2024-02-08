from django.db import models

# Create your models here.
class review(models.Model):
    username = models.CharField( max_length=50)
    feedback = models.TextField()
    ratings = models.IntegerField()
    favourite_color = models.CharField( max_length=20,blank=True)

    def __str__(self):
        return self.username