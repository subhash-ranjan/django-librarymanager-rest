from django.db import models


class Book (models.Model):
    title = models.CharField(max_length=255)
    num_pages = models.IntegerField(default=0)
    color = models.CharField(max_length=32, blank=True, null=True)
    publish_date = models.DateField(blank=True, null=True)
    price = models.DecimalField(
        decimal_places=2, max_digits=8, blank=True, null=True)
    isbn = models.CharField(max_length=13, blank=True, null=True)

    def __str__(self):
        return self.title
