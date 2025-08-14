from django.urls import path
from .views import JobListApiView, JobDetailApiView


urlpatterns = [
    path('jobs/', JobListApiView.as_view(), name='jobs'),
    path('jobs/<int:pk>', JobDetailApiView.as_view(), name='jobs'),
]
