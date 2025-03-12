from rest_framework import generics, permissions
from .models import Job, JobApplication
from .serializers import JobSerializer, JobApplicationSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsRecruiter, IsCandidate  # Import role-based permissions

# Job List & Create API (Recruiters can post jobs, everyone can view)
class JobListCreateAPIView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_permissions(self):
        if self.request.method == "POST":  # Only recruiters can post jobs
            return [IsAuthenticated(), IsRecruiter()]
        return [permissions.AllowAny()]  # Anyone can view jobs

    def perform_create(self, serializer):
        serializer.save(recruiter=self.request.user)

# Job Detail, Update & Delete API (Only recruiters can update/delete)
class JobDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated, IsRecruiter]

# Job Application List & Create API (Only candidates can apply)
class JobApplicationListCreateAPIView(generics.ListCreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

    def get_permissions(self):
        if self.request.method == "POST":  # Only candidates can apply
            return [IsAuthenticated(), IsCandidate()]
        return [IsAuthenticated()]  # Recruiters can view applications

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)

# Job Application Detail API (Recruiters can see applications for their jobs)
class JobApplicationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]
