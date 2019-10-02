from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', views.SipaUserViewSet, base_name="users")
urlpatterns = router.urls
