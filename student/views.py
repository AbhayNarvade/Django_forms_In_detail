from django.shortcuts import render
from .models import Profile
from .forms import ProfileForms

# Create your views here.
def home (request) :
    form = ProfileForms()
    return render(request , 'student/home.html' , {'form' : form})