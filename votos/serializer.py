from rest_framework import serializers
from votos.models import Departamento

class DepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ('nombre_dep')