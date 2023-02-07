from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Blog
from .forms import blogform,ContactForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    data = Blog.objects.all()
    return render(request,"index.html",{'data':data})

@login_required(login_url='login')
def readmore(request,id):
    data = Blog.objects.get(id=id)
    return render(request,"readmore.html",{'data':data})


@login_required(login_url='login')
def addblog(request):
    if request.method == "GET":
        form = blogform()
        return render (request,'addblog.html',{'form':form})
    else:
        form = blogform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('addblog')
        else:
            messages.info(request,"Try Again")
            return redirect('addblog')
        

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request,user)
                return redirect('home')
            else:
                messages.info(request,"Invalid Username/Password")
                return redirect('login')

        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Try Matching Password')
            return redirect('signup')

    return render(request,'signup.html')

@login_required(login_url='login')
def ContactPage(request):
    if request.method == "GET":
        form = ContactForm()
        return render (request,'contactform.html',{'form':form})
    else:
        form = ContactForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('home')
        else:
            messages.info(request,"Try Again")
            return redirect('contactus')
        