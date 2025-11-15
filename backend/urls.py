from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('', views.home),        
    path('admin/', admin.site.urls),
    path('users/', views.list_users),
    path('users/create/', views.create_user),
]
