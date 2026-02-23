from django.urls import path
from .views import login_view, logout_view, home_redirect

#Define the URLconf for the polls app
urlpatterns = [
    path("", home_redirect),
    path("login/", login_view, name="login" ),
    path("logout/", logout_view, name = "logout" )
]