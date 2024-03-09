# Code I wrote
from .models import Notification

def notifications(request):
    if request.user.is_authenticated:
        return {
            'notifications': Notification.objects.filter(recipient=request.user, is_read=False)
        }
    else:
        return {}
#End of Code I wrote