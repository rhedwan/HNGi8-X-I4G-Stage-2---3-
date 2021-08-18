from django.shortcuts import render, redirect
from . forms import MessageForm
from django.contrib import messages
from .models import Message
# Create your views here.

profile = {
    'name': 'Adeyemo Ridwaan',
    'short_intro' : 'Passinate Web develop',
    'location': 'Lagos, Nigeria',
    'email': 'adesolaridwan2003@gmail.com',
    'bio':'Enthusiatice web devloper',
    'topSkills': { 
        'name':'Python',
        'description': 'I develope web site'
        },

    'otherSkills': ['SQL', 'HTML','Github', 'Git']
    

}

def resume(request):
    return render(request, 'user-profile.html', {'profile':profile })

def createMessage(request):
    form = MessageForm()
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
                        
            form.save()

            messages.success(request, 'Your message was was successfully! sent')
            return redirect('home')


    context = {'form': form}
    return render(request, 'message_form.html', context)    

def inbox(request):
    messageRequests = Message.objects.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    context = {'messageRequests': messageRequests, 'unreadCount': unreadCount}
    return render(request, 'inbox.html', context)

def viewMessage(request, pk):
    message = Message.objects.get(id=pk)

    if message.is_read == False:
        message.is_read = True
        message.save()

    context = {'message': message}
    return render(request, 'message.html', context)