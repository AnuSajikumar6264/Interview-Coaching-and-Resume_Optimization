from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved')])

    def __str__(self):
        return self.name


class ResumeFeedback(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='feedback')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.resume.name}"
