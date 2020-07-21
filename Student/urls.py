from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="homepage"),
    path("studentRegistration/", views.student_register,name="Student_Registration"),
]
