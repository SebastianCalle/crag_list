from django.db import models

# Create your models here.
class Search(models.Model):
    # Model for search
    search = models.CharField(max_length=500)
    create = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.search

    class Meta:
        verbose_name_plural = "Searches"
