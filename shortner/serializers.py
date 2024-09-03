from rest_framework import serializers
from .models import Url

class Url_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = '__all__'
        read_only_fields = ['short_url', 'clicks']