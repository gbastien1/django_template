from django.urls import path

from . import views


app_name = 'pages'
urlpatterns = [
    # ex: /
    path('', views.IndexView.as_view(), name="index")
]