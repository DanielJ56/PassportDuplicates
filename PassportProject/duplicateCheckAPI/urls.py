from django.urls import path
from . import views

urlpatterns = [
    path('',views.check_duplicate_passnum),#TODOchange name to name of cuntion
]