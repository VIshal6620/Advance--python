from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.index),
    path('<page>/', views.action),
    path('<page>/<operation>/<int:id>', views.action),
]
