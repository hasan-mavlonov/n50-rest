
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from users.views import authenticated_super_user, authenticated_view, user_detail, user_list_create, \
    unauthenticated_view

urlpatterns = [
    path('', user_list_create, name='user_list_create'),
    path('<int:pk>/', user_detail, name='user_detail'),
    path('authenticated/', authenticated_view, name='authenticated_view'),
    path('authenticated/admin/', authenticated_super_user, name='authenticated_superuser'),
    path('unauthenticated/', unauthenticated_view, name='unauthenticated_view'),
    path('token/', obtain_auth_token, name='obtain_auth_token'),
    path('', include('feedbacks.urls'), name='feedbacks'),

    ]