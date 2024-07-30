from django.urls import path
from . import views

urlpatterns = [
    path("giris", views.giris_istegi, name="giris"),
    path("cikis", views.cikis_istegi, name="cikis")
]
