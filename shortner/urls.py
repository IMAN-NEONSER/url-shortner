from django.urls import path
from . import views

app_name = "shortner"

urlpatterns = [
    path('shortner/', views.UrlShortnerView.as_view(), name='url_shortner'),
    path('<str:short_url>/', views.UrlRedirectView.as_view(), name='url-redirect'),
    path('stats/<str:short_url>/', views.UrlStatsView.as_view(), name='url-stats'),
    path('update/<str:short_url>/', views.UrlUpdateView.as_view(), name='url-update'),
    path('delete/<str:short_url>/', views.UrlDeleteView.as_view(), name='url-delete'),
]
