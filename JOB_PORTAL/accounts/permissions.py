from rest_framework.permissions import BasePermission

class IsRecruiter(BasePermission):
    """Allows only recruiters to post and manage jobs."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'recruiter'

class IsCandidate(BasePermission):
    """Allows only candidates to apply for jobs."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'candidate'
