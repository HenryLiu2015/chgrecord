from django.urls import path, include
from . import views

app_name = 'chgrecord'

urlpatterns = [
    path('chgrecord_list/', views.chgrecord_list)
]
