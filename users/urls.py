from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("", views.user_login, name="user_login"),
    path("process-login/", views.process_login, name="process_login"),
    path("sign-out/", views.sign_out, name="sign_out")
]
