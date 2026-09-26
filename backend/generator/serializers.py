from rest_framework import serializers
from .models import GenerationPolicy

class GenerateSerializer(serializers.Serializer):
    length = serializers.IntegerField(min_value=8, max_value=128)
    
class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = GenerationPolicy
        fields = ['id', 'name', 'length', 'use_symbols', 'created_at']
        