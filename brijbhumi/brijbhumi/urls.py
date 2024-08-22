from django.contrib import admin
from django.urls import path
from brij import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('form/', views.form,name="form"),
    path('success/', views.success,name="success"),
    path('register/', views.register,name="register"),
    path('login/', views.user_login,name="login"),
     
]
