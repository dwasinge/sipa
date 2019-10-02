from rest_framework import serializers
from .models import SipaUser


class SipaUserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'first_name',
            'last_name',
            'dob',
            'rank',
            'type'
        )

        model = SipaUser
