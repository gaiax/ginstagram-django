from ginstagram import views
from django.urls import path

app_name = 'ginstagram'
urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('<username>', views.Profile.as_view(), name='profile'),
]
