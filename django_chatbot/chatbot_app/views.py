from django.shortcuts import render

# Create your views here.
def chatbot_app(request):
    return render(request, 'chatbot.html')