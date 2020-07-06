from rest_framework import serializers

from .models import MotoUser


class MotoUserSerialazers(serializers.ModelSerializer):
    class Meta:
        model = MotoUser
        fields =['username', 'first_name', 'last_name', 'email']