from rest_framework import generics

from .models import cnabModel
from .serializer import CnabSerializer


class CnabView(generics.ListCreateAPIView):
    queryset = cnabModel.objects.all()
    serializer_class = CnabSerializer
