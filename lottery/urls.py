from django.urls import path

from . import views

urlpatterns = [
    path('<str:qq>/<int:k>', views.index, name='index'),
]