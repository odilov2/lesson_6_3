from django.urls import path
from .views import courses_view

urlpatterns = [
    path("courses/", courses_view, name="courses")
]