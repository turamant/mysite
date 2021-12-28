from django.shortcuts import render

# Create your views here.
from polls.models import Vote


def index(request):
    return render(request, 'polls/index.html')

def list_vote(request):
    votes = Vote.objects.all()
    context = {'votes': votes}
    return render(request, 'polls/vote_list.html', context)

