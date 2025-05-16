from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComisionViewSet, MiembroComisionViewSet

router = DefaultRouter()
router.register(r'/comisiones', ComisionViewSet)
router.register(r'/miembros', MiembroComisionViewSet)
urlpatterns = [
    path('', include(router.urls))
]
