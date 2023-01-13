from rest_framework.routers import DefaultRouter

from .views import PlayerModelViewSet

router = DefaultRouter()
router.register(r"", PlayerModelViewSet, basename="players")

urlpatterns = router.urls
