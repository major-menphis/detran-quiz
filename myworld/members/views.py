from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

def index(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    a = request.POST['fullName']
    b = request.POST['email']
    member = Members(fullName=a, email=b, points=0, quizResolved=0, questionsResolved=0)
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    a = request.POST['fullName']
    b = request.POST['email']
    member = Members.objects.get(id=id)
    member.fullName = a
    member.email = b
    member.save()
    return HttpResponseRedirect(reverse('index'))

# Create your views here.
