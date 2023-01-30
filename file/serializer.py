from rest_framework import serializers

from cnab.models import cnabModel
from trades.models import tradesModel

from .convert import convert_data
from .models import fileModel


class fileSerializer(serializers.ModelSerializer):
    class Meta:

        model = fileModel
        fields = ["file"]
        extra_kwargs = {"file": {"write_only": True}}

    def create(self, validated_data):

        result = convert_data(validated_data["file"])

        for value in result:
            trade = {}
            trade["Dono_da_loja"] = value.pop("Dono_da_loja")
            trade["Nome_loja"] = value.pop("Nome_loja")

            trade_create, created = tradesModel.objects.get_or_create(**trade)
            trade_id = trade_create.id
            value["trades_id"] = trade_id
            cnabModel.objects.create(**value)
        return cnabModel.objects.filter(trades_id=trade_id)
