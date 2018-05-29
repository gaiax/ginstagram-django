from ginstagram import views
from django.urls import path

app_name = 'ginstagram'
urlpatterns = [
    path('registration/', views.Registration.as_view(), name='registration'),
    path('<username>/', views.Profile.as_view(), name='profile'),
    path('icon/edit/<username>/', views.ProfileIcon.as_view(), name='icon'),
]
