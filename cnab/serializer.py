from rest_framework import serializers

from .models import cnabModel


class CnabSerializer(serializers.ModelSerializer):
    class Meta:

        model = cnabModel
        fields = "__all__"

        
    
     