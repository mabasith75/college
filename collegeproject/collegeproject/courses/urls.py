from django.urls import path
from . import views
app_name = 'courses'

urlpatterns = [
    path('courses/', views.details, name='details'),
    path('', views.order, name='order')
]