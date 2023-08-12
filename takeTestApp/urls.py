from django.urls import path
from .views import find_available_test_centers, Home

urlpatterns = [
    path('', Home, name="Home Page"),
    path('test_center', find_available_test_centers, name="Find Test Centers"),
]