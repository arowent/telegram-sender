from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('profile/', TemplateView.as_view(template_name='account/profile.html'))
]
