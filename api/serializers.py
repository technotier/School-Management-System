from rest_framework import serializers

class ResultInfoSerializer(serializers.Serializer):
    board = serializers.CharField(max_length=12)
    roll = serializers.IntegerField()