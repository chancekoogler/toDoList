from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("chance", views.chance, name="chance"),
    path("<str:name>", views.greet, name="greeting")

]