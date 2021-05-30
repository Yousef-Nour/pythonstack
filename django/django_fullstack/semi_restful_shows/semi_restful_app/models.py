from django.db import models

class Series(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




def add_new(title,network,release_date,desc):

    Series.objects.create(title=title,network=network,release_date=release_date,desc=desc)
    series_id = Series.objects.last()
    return series_id.id