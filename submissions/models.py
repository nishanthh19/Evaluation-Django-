from django.db import models

class Submission(models.Model):
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField()
    code = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    result = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.student_name} - {self.result}"
