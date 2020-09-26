from django.urls import path
from .views import CustomUserCreate

app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),
]
