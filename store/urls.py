from django.urls import path

from .views import store_home, store_charts


app_name = "store"


urlpatterns = [
    path("", store_home, name="home"),
    path("charts/", store_charts, name="charts"),
]
