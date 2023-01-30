from rest_framework import generics

from .models import fileModel
from .serializer import fileSerializer

class fileView(generics.ListCreateAPIView):
    queryset = fileModel.objects.all()
    serializer_class = fileSerializer
