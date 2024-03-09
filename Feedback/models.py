from django.db import models
# Code I wrote
from django.conf import settings
from courses.models import Course

# Create your models here.
class Feedback(models.Model):
    course = models.ForeignKey(Course, related_name='feedback', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='feedback', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Feedback by {self.user.username} on {self.course.title}'
# End of Code I wrote