from django.urls import path
from Kontrol import views

urlpatterns = [
    path('first', views.first_page),
    path('second', views.second_page)
]