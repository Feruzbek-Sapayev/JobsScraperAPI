from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from .models import Job
from .serializers import JobSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView


class JobPagination(PageNumberPagination):
    page_size = 5 
    page_size_query_param = 'page_size'
    max_page_size = 100


class JobListApiView(ListAPIView):
    queryset = Job.objects.all().order_by('-posted_at')
    serializer_class = JobSerializer
    pagination_class = JobPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'company', 'location', 'tags']


class JobDetailApiView(RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer