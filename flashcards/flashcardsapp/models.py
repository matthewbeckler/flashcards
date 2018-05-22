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


class Interaction(models.Model):
    """ A record of an interaction of a user and a card. """
    # TODO figure out how to do user stuff, for now assume one user
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    success = models.BooleanField(default=False)

    def __str__(self):
        return "%s, %s, %s" % ("USER", self.card, self.timestamp)
