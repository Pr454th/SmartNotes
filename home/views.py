from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    print(date)
    return render(request,'home/welcome.html',{'today':date.today()})

#authorize page
#Cannot access this page unless you are logged in django admin
@login_required(login_url='/admin')
def authorized(request):
    return render(request,'home/authorized.html',{})

#simple response page
# def home(request):
#     return HttpResponse('hello world')