from django.urls import path
from dishes.views import menu_list_create, menu_detail

urlpatterns = [
    path('', menu_list_create, name='dish_list_create'),
    path('<int:pk>/', menu_detail, name='dish_list_create'),
]