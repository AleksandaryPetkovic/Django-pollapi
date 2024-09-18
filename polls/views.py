from rest_framework import generics
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Poll, Choice
from .serializers import PollSerializer,ChoiceSerializer, VoteSerializer


def polls_list(request):
    MAX_OBJECTS =20
    polls =Poll.objects.all()[:MAX_OBJECTS]
    data={"resluts": list(polls.values("question", "created_by__username", "pub_date"))}
    return JsonResponse(data)
# class PollList(generics.ListCreateAPIView):
#     queryset = Poll.objects.all()
#     serializer_class = PollSerializer
def polls_detail(request,pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {
        "result":{
            "question": poll.question,
            "created_by": poll.created_by.username,
            "pub_date": poll.pub_date
        }
    }
    return JsonResponse(data)
# class PollDetail(generics.RetrieveDestoryAPIView):
#     queryset = Poll.objects.all()
#     serializer_class = PollSerializer

# class ChoiceList(generics.ListCreateAPIView):
#     queryset = Choice.objects.all()
#     serializer_class = ChoiceSerializer
    
# class CreateVote(generics.CreateAPIView):
#     serializer_class = VoteSerializer
