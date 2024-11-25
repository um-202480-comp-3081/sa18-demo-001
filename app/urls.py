from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
  path('customers/', views.customer_list, name='customers')
]