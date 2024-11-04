from django.urls import path

from feedbacks import views

urlpatterns = [
    path('feedbacks/', views.feedback_list_create, name='feedbacks'),
    path('feedbacks/<int:pk>/', views.feedback_detail, name='feedback_detail'),
]