from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.city_form),
    path('cities_list/', views.cities_list)
]