from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('test-viewset', views.TestViewSet, basename='test-viewset')

urlpatterns = [
    path('testapi/', views.TestApiView.as_view()),
    path('', include(router.urls))
]
