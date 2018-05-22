from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('card/<int:card_id>/', views.card, name='card'),
    path('deck/<int:deck_id>/', views.deck, name='deck'),

    # backend endpoints
    path('json/card/<int:card_id>/', views.json_card, name='json_card'),
    path('json/deck/<int:deck_id>/', views.json_deck, name='json_deck'),
    path('json/similar_cards/<int:card_id>/<int:atob>/<int:num_other_cards>/', views.json_similar_cards, name='json_similar_cards'),
]

