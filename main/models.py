from django.db import models
from django.utils import timezone
from markupfield.fields import MarkupField

class Recipe (models.Model):
    title = models.CharField(max_length=128);
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_published = models.DateTimeField(default=timezone.now)
    method = MarkupField(default_markup_type='markdown')

class Rating (models.Model):
    value = models.PositiveSmallIntegerField(null=True)
    comment = models.TextField()
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)

