from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.
@login_required(login_url='login')
def ChatRoom(request, username):
    receiver = User.objects.filter(username=username).first()
    
    if request.POST:
        messages = request.POST.get('message')
        if messages:
            Message.objects.create(sender=request.user, receiver=receiver, content=messages)
  
        return redirect('ChatRoom', username=username)

    messages = Message.objects.filter(sender=request.user, receiver=receiver).order_by('timestamp') | Message.objects.filter(sender=receiver, receiver=request.user).order_by('timestamp')
    
    return render(request, 'chat/chat.html', {'receiver': receiver, 'messages': messages})