from django.urls import path

from . import views

app_name = 'shipping'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:shipment_id>', views.detail, name='detail')
]
