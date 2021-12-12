
from rest_framework import serializers


class SearchParamsSerializer(serializers.Serializer):
    query = serializers.CharField()
