from rest_framework import serializers

from .models import tradesModel


class tradesSerializer(serializers.ModelSerializer):
    saldo = serializers.SerializerMethodField()

    class Meta:

        model = tradesModel
        fields = "__all__"
        extra_kwargs = {"__all__": {"write_only": True}}

    def get_saldo(self, obj):
        cnab_set = obj.cnab.all()
        value_total = 0
        for cnab in cnab_set:
            value = cnab.Valor
            value_total += value
        return value_total
