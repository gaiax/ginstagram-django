from ginstagram import views
from django.urls import include, path

urlpatterns = [
    path('', views.main),
    path('login', views.login),
]
