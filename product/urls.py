from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, login, signup, test_token, RegisterUserView, LoginUserView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path('login/', LoginUserView.as_view(), name='login'),
    re_path('signup', RegisterUserView.as_view(), name='signup'),
    re_path('test_token', test_token),
]
