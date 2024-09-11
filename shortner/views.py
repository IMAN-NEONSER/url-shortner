from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Url
from rest_framework import status
from .serializers import UrlSerializer

# Create your views here.
class UrlShortnerView(APIView):
    def post(self, request):
        serializer = UrlSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UrlRedirectView(APIView):
    def get(self, request, short_url):
        url = get_object_or_404(Url, short_url=short_url)
        url.clicks += 1
        url.save()
        return redirect(url.original_url)

class  UrlStatsView(APIView):
    def get(self, request, short_url):
        url = get_object_or_404(Url, short_url=short_url)
        serializer = UrlSerializer(url)
        return Response(serializer.data)

