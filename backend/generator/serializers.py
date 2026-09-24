from rest_framework import serializers

class GenerateSerializer(serializers.Serializer):
    length = serializers.IntegerField(min_value=8, max_value=128)
    
    