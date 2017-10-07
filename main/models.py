from django.db import models
from django.utils import timezone
from markupfield.fields import MarkupField

class Recipe (models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_published = models.DateTiemField(default=timezone.now)
    method = MarkupField(default_markup_type='markdown')

class Rateing (models.Model):
    value = PositiveSmallIntegerField()
    comment = TextField()
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)

