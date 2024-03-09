from django.db import models
# Code I wrote
from courses.models import Course # access to course model

# Create your models here.
class Material(models.Model):
    course = models.ForeignKey(Course, related_name='materials', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='course_materials/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
# End of Code I wrote
