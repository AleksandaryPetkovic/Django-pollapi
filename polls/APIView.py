from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Poll, Choice
from .serializers import PollSerializer
from rest_framework import generics
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer

class PollList(APIView):
    def get(self, request):
        polls = Poll.objects.all()[:20]
        data = PollSerializer(polls, many=True).data
        return Response(data)
# class PollDetail(APIView):
#     def get(self, request, pk):
#         poll = get_object_or_404(Poll, pk=pk)
#         data = PollSerializer(poll).data
#         return Response(data)
class PollDetail(generics.RetrieveDestroyAPIView): # only post method
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class ChoiceList(generics.ListCreateAPIView): # get and post method
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    
class CreateVote(generics.CreateAPIView):
    serializer_class = VoteSerializer
    