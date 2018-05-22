from django.contrib import admin

from .models import Card, Deck, Interaction

admin.site.register(Card)
admin.site.register(Deck)
admin.site.register(Interaction)
