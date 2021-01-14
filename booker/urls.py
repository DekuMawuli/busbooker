from django.urls import path
from . import views

app_name = "booker"
urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard")
]
