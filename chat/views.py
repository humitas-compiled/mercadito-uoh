from django.shortcuts import render

# Create your views here.

def mis_chats(request):
    return render(request, 'main/chats.html')
