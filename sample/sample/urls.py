from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app1.views import StudentView
router=DefaultRouter()
router.register('student',StudentView,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
]
