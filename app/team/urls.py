from django.urls import path, include
from rest_framework import routers
from .views import PersonViewSet, TeamViewSet


router = routers.DefaultRouter()
router.register(r'teams', TeamViewSet, basename="teams")
router.register(r'person', PersonViewSet, basename="person")

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]