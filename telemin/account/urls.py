from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('profile/', views.get_posts, name='profile'),
    # path('register/', views.UserView.as_view(), name='users'),
]
