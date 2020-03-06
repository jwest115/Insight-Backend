from django.urls import path, include
from rest_framework import routers
from knox import views as knox_views

from accounts.api import UserAPI, UsersViewSet, RegisterAPI, LoginAPI

urlpatterns = [
  path('api/accounts/user', UserAPI.as_view()),
  path('api/accounts/register', RegisterAPI.as_view()),
  path('api/accounts/login', LoginAPI.as_view()),
  path('api/accounts/logout', knox_views.LogoutView.as_view(), name='knox_logout')
]


router = routers.DefaultRouter()
router.register('api/accounts/users', UsersViewSet, 'user')
router.register('api/accounts/users/<int:user_id>/', UsersViewSet, 'user')
urlpatterns += router.urls