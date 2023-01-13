from rest_framework.routers import DefaultRouter

from .views import TeamModelViewSet

router = DefaultRouter()
router.register(r"", TeamModelViewSet, basename="teams")

urlpatterns = router.urls
