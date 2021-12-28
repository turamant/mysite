from django.db import models



class Vote(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    poster = models.ImageField(upload_to='posters/', blank=True)

    def __str__(self):
        return self.title
