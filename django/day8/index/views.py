from django.shortcuts import render

# Create your views here.
def register_views(request):
    return render(request,"01_register.html")