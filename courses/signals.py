# Code I wrote

from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Course
from Notifications.models import Notification  # Adjust the import based on your project structure

@receiver(m2m_changed, sender=Course.enrolled_students.through)
def notify_teacher_on_new_enrollment(sender, instance, action, pk_set, **kwargs):
    """
    Notify the course's teacher whenever a new student enrolls.
    """
    if action == "post_add":  # Check if it's a new addition
        # Fetch the teacher
        teacher = instance.teacher

        # Fetch the student(s) just added
        from django.contrib.auth import get_user_model
        User = get_user_model()
        students = User.objects.filter(pk__in=pk_set)

        # Create a notification for each student added (or a single notification summarizing the addition)
        for student in students:
            Notification.objects.create(
                user=teacher,
                message=f"{student.username} has enrolled in your course: {instance.title}."
            )

# End of Code I wrote