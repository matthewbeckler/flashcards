import datetime

from django.db import models
from django.utils import timezone


class Deck(models.Model):
    title = models.CharField(max_length=200)
    update_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def was_updated_recently(self):
        return self.update_date >= (timezone.now() - datetime.timedelta(days=1))


class Card(models.Model):
    sidea = models.CharField(max_length=200)
    sideb = models.CharField(max_length=200)
    update_date = models.DateTimeField()
    reversable = models.BooleanField(default=False)
    decks = models.ManyToManyField(Deck)

    def __str__(self):
        s = self.sidea
        s += " <-> " if self.reversable else " -> "
        s += self.sideb
        return s

    def was_updated_recently(self):
        return self.update_date >= (timezone.now() - datetime.timedelta(days=1))

