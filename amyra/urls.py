from django.urls import path
from . import views

app_name = "amyra"

urlpatterns = [
    path('', views.index, name="index"),
    path('customers/', views.customers, name="customers")
]