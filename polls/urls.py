from django.urls import path

from polls.views import index

from polls.views import list_vote

urlpatterns = [
    path('', index, name='index'),
    path('votes/', list_vote, name='list_vote')
]