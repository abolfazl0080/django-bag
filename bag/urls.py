from django.urls import path
from . import views

urlpatterns = [
    path('', views.BagListCreateApi.as_view()),
    path('<int:pk>/', views.BagGetUpdateDeleteApi.as_view()),
    path('images/', views.ImageOfBagCreateApi.as_view()),
    path('category/', views.CategoryListCreateApi.as_view()),
    path('category/<int:pk>/', views.CategoryGetUpdateDeleteApi.as_view()),
    path('label/', views.LabelListCreateApi.as_view()),
    path('label/<int:pk>/', views.LabelGetUpdateDeleteApi.as_view()),
]
