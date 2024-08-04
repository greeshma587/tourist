from django.shortcuts import render,redirect,get_object_or_404
from . models import *
from .models import Tourist
from rest_framework import generics
from . serializers import *
from rest_framework . permissions import AllowAny
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == 'POST':
       
        spotname = request.POST.get("spotname")
        place = request.POST.get("place")
        city = request.POST.get("city")
        state = request.POST.get("state")
        country = request.POST.get("country")
        spotimage = request.FILES.get("spotimage")
        googlemap = request.POST.get("googlemap")

        user = Tourist(spotname=spotname,place=place,city=city,state=state,country=country,spotimage=spotimage,googlemap=googlemap)
        user.save()
        return redirect('index')

    tourist_spot = Tourist.objects.all()

    return render(request, 'index.html', {'tourist_spots': tourist_spot})

def details(request, id):
    tourist_spot = get_object_or_404(Tourist, id=id)

    return render(request, 'view.html', {'tourist_spot': tourist_spot})

def update(request,id):
   
    tourist_spot = get_object_or_404(Tourist,id=id)

    if request.method == 'POST':
        
        
        spotname = request.POST.get("spotname")
        place = request.POST.get("place")
        city = request.POST.get("city")
        state = request.POST.get("state")
        country = request.POST.get("country")
        spotimage = request.POST.get("spotimage")
        googlemap = request.POST.get("googlemap")

        tourist_spot.spotname = spotname
        tourist_spot.place = place
        tourist_spot.city = city
        tourist_spot.state = state
        tourist_spot.country = country
        if spotimage:  
            tourist_spot.spotimage = spotimage
        tourist_spot.googlemap = googlemap
        tourist_spot.save()

       
        return redirect('index')

    
    return render(request, 'index.html', {'tourist_spot': tourist_spot})

def delete(request, id):
    
    tourist_spot = get_object_or_404(Tourist, id=id)
    
    if request.method == 'POST':
        
        tourist_spot.delete()
        
        messages.success(request, "Tourist record deleted successfully.")
        
        return redirect('index')
    
    
    return render(request, 'index.html', {'tourist_spot': tourist_spot})






