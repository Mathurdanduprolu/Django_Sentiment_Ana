# sentimentapp/urls.py
from django.urls import path
from .views import analyze_view, analyze_page

urlpatterns = [
    path('analyze/', analyze_view, name='analyze'),
    path('', analyze_page, name='analyze_page'),
]
