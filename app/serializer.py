from rest_framework import serializers
from .models import user

class userserializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['id', 'firstname', 'lastname']
