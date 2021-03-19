from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method =="POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        return render(request, 'contact.html', {'message_name':message_name})

        #send an Email
        send_mail(message_name,
            message,
            message_email,
            ['vcaredentalclinic121@gmail.com'],
            fail_silently = False,
            )


    else:
        return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})


def service(request):
    return render(request, 'service.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})
