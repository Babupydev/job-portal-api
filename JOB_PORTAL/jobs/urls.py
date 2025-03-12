from django.urls import path
from .views import JobListCreateAPIView, JobDetailAPIView, JobApplicationListCreateAPIView, JobApplicationDetailAPIView

urlpatterns = [
    path('jobs/', JobListCreateAPIView.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', JobDetailAPIView.as_view(), name='job-detail'),
    path('applications/', JobApplicationListCreateAPIView.as_view(), name='job-application-list'),
    path('applications/<int:pk>/', JobApplicationDetailAPIView.as_view(), name='job-application-detail'),
]
