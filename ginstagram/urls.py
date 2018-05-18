from ginstagram import views
from django.urls import include, path

urlpatterns = [
    path('', views.main),
    path('<user_name>/', views.profile, name='profile'),

]
