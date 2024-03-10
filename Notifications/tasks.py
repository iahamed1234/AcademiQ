from celery import shared_task
from django.contrib.auth import get_user_model
from .models import Notification

@shared_task
def notify_users_about_new_material(course_id, material_id):
    User = get_user_model()
    users = User.objects.filter(enrolled_courses__id=course_id)
    for user in users:
        Notification.objects.create(
            user=user,
            message=f"New materials have been added to your course.",
        )