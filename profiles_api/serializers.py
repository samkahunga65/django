from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """serializes a name forr testing our api view"""
    name = serializers.CharField(max_length=10)