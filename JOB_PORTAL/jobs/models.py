from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Job(models.Model):
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posted_jobs")
    title = models.CharField(max_length=255)
    description = models.TextField()
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    employment_type = models.CharField(
        max_length=50, 
        choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Contract', 'Contract'), ('Internship', 'Internship')]
    )
    experience_level = models.CharField(
        max_length=50,
        choices=[('Entry', 'Entry'), ('Mid', 'Mid'), ('Senior', 'Senior')],
        default='Entry'
    )
    skills_required = models.CharField(max_length=500, help_text="Comma-separated skills (e.g., Python, Django, REST API)")
    education_required = models.CharField(max_length=255, null=True, blank=True)
    job_responsibilities = models.TextField()
    job_requirements = models.TextField()
    benefits = models.TextField(null=True, blank=True)
    application_deadline = models.DateField(null=True, blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    linkedin_profile = models.URLField(null=True, blank=True)
    portfolio_url = models.URLField(null=True, blank=True)
    expected_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    available_start_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=50,
        choices=[('Pending', 'Pending'), ('Reviewed', 'Reviewed'), ('Rejected', 'Rejected'), ('Accepted', 'Accepted')],
        default='Pending'
    )
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.email} applied for {self.job.title}"
