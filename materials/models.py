from django.db import models
# Code I wrote
from courses.models import Course
from Notifications.models import Notification


# Create your models here.
class Material(models.Model):
    course = models.ForeignKey(Course, related_name='materials', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='course_materials/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
# Signal that a new material is saved
def material_added_notification(sender, instance, created, **kwargs):
    if created:  # Check if a new instance was created
        course = instance.course
        students = course.enrolled_students.all()
        for student in students:
            Notification.objects.create(
                recipient=student,
                message=f"New material added to {course.title}: {instance.title}"
            )
# End of Code I wrote
