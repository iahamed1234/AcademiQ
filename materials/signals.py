# Code I wrote
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Material
from Notifications.models import Notification

@receiver(post_save, sender=Material)
def material_added(sender, instance, created, **kwargs):
    if created:
        course = instance.course
        teacher = course.teacher
        students = course.enrolled_students.all()
        for student in students:
            Notification.objects.create(
                recipient=student,
                message=f'New material added to {course.title} by {teacher.username}.'
            )

# End of Code I wrote