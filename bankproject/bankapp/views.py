from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect

from .forms import regform
from .models import registration
import cgi
# from .models import department,employee
from django.core import serializers
# Create your views here.
def demo(request):
    return render(request,"index.html")

def index(request):
   return render(request,"index.html")
def loginreg(request):

  return render(request,'loginreg.html')

# def login(request):
#     if request.method=='POST':
#         username=request.POST["username"]
#         password=request.POST["password"]
#         user=auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect("/")
#         else:
#             messages.info(request,"invalid credentials")
#             # return redirect("loginreg.html")
#     return render(request,"login.html")
def login(request):
    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid credentials")
            # return redirect("login/")
    return render(request,"login.html")

def reglog(request):
    if request.method=='POST':
        uname=request.POST["username"]
        password=request.POST["password"]
        cpassword=request.POST["password1"]
        if password == cpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"username already exist")
                return redirect("bankapp:reglog")
            elif User.objects.filter(password=password).exists():
                messages.info(request,"this pwd id already exist")
                return redirect("bankapp:reglog")
            else:
                user = User.objects.create_user(username=uname,password=password)
                user.save()
                print("user created")
                return redirect("bankapp:login")
        else:
            messages.info(request,"password not matching")
            return redirect("bankapp:reglog")
        return redirect("bankapp:login")
    return render(request,'reglog.html')

def registrations(request):


    task1 = registration.objects.all()
    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        ph = request.POST['ph']
        dob = request.POST['dob']
        gender = request.POST['gender']
        address = request.POST['address']
        state = request.POST['state']
        district = request.POST['district']
        branch = request.POST['branch']
        actype = request.POST['actype']
        material = request.POST['material']
        # if password == cpassword:
        # if User.objects.filter(username=name).exists():
        #      # messages.info(request, "username already exist")
        #      return redirect("bankapp:registration")
        # elif User.objects.filter(email=email).exists():
        #         # messages.info(request, "this email id already exist")
        #         return redirect("bankapp:registration")
        # else:
        t1=registration(name=name,email=email,ph=ph,dob=dob,gender=gender,address=address,state=state,
                                                district=district,branch=branch,actype=actype,material=material)
        t1.save()
        print("user created")
        messages.info(request,"happy")
        return redirect("bankapp:registration")
        return redirect("login")
    return render(request,'registration.html',{'task11': task1})
























        # if request.method == 'POST':
        #     name = request.POST['name']
        #     email = request.POST['email']
        #     ph = request.POST['ph']
        #     dob = request.POST['dob']
        #     gender = request.POST['gender']
        #     address = request.POST['address']
        #     state = request.POST['state']
        #     district = request.POST['district']
        #     branch = request.POST['branch']
        #     actype = request.POST['actype']
        #     material = request.POST['material']
        #     if name != email:
        #         if User.objects.filter(username=name).exists():
        #             messages.info(request, "username already exist")
        #             return redirect("bankapp:registration")
        #         elif User.objects.filter(email=email).exists():
        #             messages.info(request, "this email id already exist")
        #             return redirect("bankapp:registration")
        #         else:
        #             user = User.objects.create_user(username=name, email=email, ph=ph, dob=dob, gender=gender,
        #                                             address=address,
        #                                             state=state, district=district, branch=branch, actype=actype,
        #                                             material=material)
        #             user.save()
        #             print(user)
        #     else:
        #         messages.info(request, "invalid")
        #         return render(request, 'registration.html')
        #     return redirect("bankapp:registration")
        # return render(request,'registration.html')
        #

def logout(request):
    auth.logout(request)
    return redirect('/')


