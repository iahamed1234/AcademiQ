from django.shortcuts import render

# Create your views here.
def chat_room(request, room_name):

    # Renders the chat room page with a specific room name.
    return render(request, 'communication/chat_room.html', {
        'room_name': room_name
    })