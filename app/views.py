from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,"index.html",{})

def show_user(request,name,user_id):
    message = {'message':'hello ' + name + str(user_id)}
    return render(request,"index.html",message)