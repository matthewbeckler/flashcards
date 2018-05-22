from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse

from .models import Card, Deck, Interaction

def index(request):
    return HttpResponse("Hello world, from flashcardsapp index.")

def card(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    return HttpResponse("You're looking at card %d: %s" % (card_id, card))

def deck(request, deck_id):
    return HttpResponse("You're looking at deck %d." % deck_id)


# backend endpoints
def json_card(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    return JsonResponse({'card_id': card.id,
                         'sidea': card.sidea,
                         'sideb': card.sideb})

def json_deck(request, deck_id):
    card = get_object_or_404(Card, pk=card_id)
    return JsonResponse({'foo': 'bar'})

#def json_add_interaction(request)

def json_similar_cards(request, card_id, atob, num_other_cards):
    card = get_object_or_404(Card, pk=card_id)

    # TODO abstract "is similar" to a helper function?
    if atob:
        similar = Card.objects.filter(sidea__startswith=card.sidea[0])[:num_other_cards]
    else:
        similar = Card.objects.filter(sideb__startswith=card.sidea[0])[:num_other_cards]

    similar_card_ids = []
    for s in similar:
        similar_card_ids.append(s.id)
    return JsonResponse(similar_card_ids, safe=False)




