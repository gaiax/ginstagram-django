from ginstagram import views
from django.urls import include, path

app_name = 'ginstagram'
urlpatterns = [
    path('', views.main),
    path('registration/', views.registration, name='registration'),
    path('<user_name>/', views.profile, name='profile'),
]
