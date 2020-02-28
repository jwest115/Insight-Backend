from django.urls import path, include
from rest_framework import routers

from accounts.api import UserAPI, UsersViewSet

urlpatterns = [
  path('api/accounts/user', UserAPI.as_view()),
]


router = routers.DefaultRouter()
router.register('api/accounts/users', UsersViewSet, 'user')
router.register('api/accounts/users/<int:pin_id>/', UsersViewSet, 'user')
urlpatterns += router.urls