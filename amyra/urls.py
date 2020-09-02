from django.urls import path
from . import views

app_name = "amyra"

urlpatterns = [
    path('', views.index, name="index"),
    path('customers/', views.customers, name="customers"),
    path('customers/add_customer/', views.add_customer, name="add_customer"),
    path('customers/remove_customer/', views.remove_customer, name="remove_customer"),
    path('customers/edit_customer/', views.edit_customer, name="edit_customer"),
]