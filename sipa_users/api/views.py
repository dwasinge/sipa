from rest_framework import viewsets
from user.models import SipaUser
from user.serializers import SipaUserSerializer


class SipaUserViewSet(viewsets.ModelViewSet):
    queryset = SipaUser.objects.all()
    serializer_class = SipaUserSerializer
