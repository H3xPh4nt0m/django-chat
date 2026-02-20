from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required(login_url='login')
def ChatRoom(request, username):
    receiver = User.objects.filter(username=username).first()
    
    if request.POST:
        messages = request.POST.get('message')
        if messages:
            Message.objects.create(sender=request.user, receiver=receiver, content=messages)
  
    
    messages = Message.objects.filter(sender=request.user, receiver=receiver).order_by('timestamp') | Message.objects.filter(sender=receiver, receiver=request.user).order_by('timestamp')
    
    return render(request, 'chat/chat.html', {'receiver': receiver, 'messages': messages})