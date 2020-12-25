from django.contrib import admin
from django.urls import path
from kkk import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.login, name="login"),
    path('insert/', views.insert),
    path('show/', views.show, name="show"),
    path('one_insert/', views.one_insert, name="one"),
    path('delete/<id>/', views.delete, name="delete"),
    path('update/<id>/', views.update, name="update"),




]
