from django.http import HttpResponse

from user.models import SipaUser


def health(request):
    return HttpResponse(SipaUser.objects.count())
