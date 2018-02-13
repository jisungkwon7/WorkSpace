from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import contactForm

# Create your views here.
def contact(request):
    title = 'Contact'
    form = contactForm(request.POST or None)
    context = {'title':title,'form':form}
    if form.is_valid():
        print(form.cleaned_data['email'])
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message form MYSITE.com'
        emailFrom = form.cleaned_data['email']
        emailto = [settings.EMAIL_HOST_USER]
        message = '%s %s %s' %(comment, name, emailFrom)
        send_mail(subject,message,emailFrom,emailto,fail_silently=True )
        title = "Thanks!"
        confirm_message = "Thanks for the message. We will ge right back to you."
        context = {'title':title,'confirm_message':confirm_message,}
    # context = locals()
    template = 'contact.html'
    return render(request,template,context)
