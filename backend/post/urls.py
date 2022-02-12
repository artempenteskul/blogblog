from django.urls import path

from .views import home


app_name = 'post'

urlpatterns = [
    path('home/', home, name='home'),
]
