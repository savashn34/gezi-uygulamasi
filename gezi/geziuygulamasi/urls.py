from django.urls import path
from django.contrib.auth.views import PasswordChangeView
from . import views

urlpatterns = [
    path("", views.index, name="baslangic"),
    path("geziler", views.geziler, name="geziler"),
    path("geziciler", views.geziciler, name="geziciler"),
    path("geziciler/<slug:slug>", views.gezici, name="gezici"),
    path("gezgin/<slug:slug>", views.gezgin, name="gezgin"),
    path("gezginler", views.gezginler, name="gezginler"),
    path("takimlar", views.takimlar, name="takimlar"),
    path("gecmis", views.gecmis, name="gecmis"),
    path("gelecek", views.gelecek, name="gelecek"),
    path("<slug:slug>", views.takim, name="takim"),
    path('accounts/password_change/', PasswordChangeView.as_view(), name='password_change'),
]
