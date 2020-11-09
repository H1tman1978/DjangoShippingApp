from django.urls import path

from . import views

app_name = 'shipping'
urlpatterns = [
    path('', views.ListShipment.as_view()),
    path('<int:pk>/', views.DetailShipment.as_view()),
    path('package/', views.ListPackage.as_view()),
    path('package/<int:pk>', views.DetailPackage.as_view()),
    path('part/', views.ListPart.as_view()),
    path('part/<int:pk>/', views.DetailPart.as_view()),
    path('machine/', views.ListMachine.as_view()),
    path('machine/<int:pk>', views.DetailMachine.as_view()),
]
