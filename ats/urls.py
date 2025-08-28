from django.urls import path

from .views import ats_home, ats_results

app_name = "ats"

urlpatterns = [
    path("", ats_home, name="home"),
    path("results/", ats_results, name="results"),
]
