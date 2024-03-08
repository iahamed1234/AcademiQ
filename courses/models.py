from django.db import models
# Code I wrote
from django.conf import settings

# Create your models here.
# Course model with many to many relationship and foreign key to user model for course teacher
from django.db import models
from django.conf import settings

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # This ensures compatibility with custom user models
        on_delete=models.CASCADE,
        related_name='taught_courses'
    )
    enrolled_students = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='enrolled_courses',
        blank=True  # Students can be enrolled in a course optionally
    )

    def __str__(self):
        return self.title



# End of Code I wrote