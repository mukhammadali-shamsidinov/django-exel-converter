from django.urls import path
from .views import UserView
app_name="user"
urlpatterns = [
    path('users/',UserView.as_view(),name="user"),
]