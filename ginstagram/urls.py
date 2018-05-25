from ginstagram import views
from django.urls import include, path

app_name = 'ginstagram'
urlpatterns = [
    path('', views.main),
    path('<user_name>/', views.profile, name='profile'),
]
