from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Person
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.db.utils import IntegrityError
import os
from .__init__ import path

photo_path = path + 'website/photos/'

class Home(View):

    template_name = 'website/home.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        un = request.POST["username"]
        pw = request.POST["password"]

        u = authenticate(username = un, password = pw)
        if u is not None:
            login(request, u)
            p = Person.objects.filter(user = u).first()
            if p.designation == 1: # 1: Employee, 2: Security, 3: Admin
                return render(request, 'website/employee.html')
            elif p.designation == 2:
                return render(request, 'website/security.html')
            elif p.designation == 3:
                return render(request, 'website/admin.html')
        else:
            return HttpResponse('Fail')

class SignUp(View):
    
    template_name = 'website/signup.html'

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else: return render(request, "website/home.html")

    def post(self, request):
        try:
            p = Person()
            user = User()
            user.username = request.POST['username']
            user.set_password(request.POST['password'])
            user.first_name = request.POST['name']
            user.save()
            p.user = user
            p.designation = request.POST['designation']

            if int(p.designation) == 3:
                user.is_staff = True
                user.is_admin = True
                user.is_superuser = True
                user.save()
            p.save()
        except IntegrityError:
            err = {'error', 'Username already exists!'}
            return render(request, self.template_name, err)

        return render(request, 'website/home.html')

def Logout(request):
    logout(request)
    return redirect('website:Home')