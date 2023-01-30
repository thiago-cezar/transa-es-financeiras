from rest_framework import generics

from .models import tradesModel
from .serializer import tradesSerializer


class tradesView(generics.ListCreateAPIView):
    queryset = tradesModel.objects.all()
    serializer_class = tradesSerializer
    