from django.urls import path
from . import views

app_name = 'shortner'
urlpatterns = [
    path('shortner/', views.UrlShortnerView.as_view(), name='url_shortner'),
]