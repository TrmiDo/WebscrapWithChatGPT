from django.urls import path
from . import views
urlpatterns =[
    path("webscrap/", views.index2, name="webscrap"),
    path("", views.home, name="home"),
]