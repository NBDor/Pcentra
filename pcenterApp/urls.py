from django.urls import path
from . import views

appname = "shortcut"

urlpatterns = [
    path('create', views.create),
    path('<str:query>', views.redirect_url_view, name='redirect'),
]