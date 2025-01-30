from django.shortcuts import render , redirect
from .models import Profile
from .forms import ProfileForms
from django.http import HttpResponse 

# Create your views here.
def home(request):
    if request.method == "POST":
        # Initialize the form with POST data and files
        form = ProfileForms(request.POST, request.FILES)
        
        # Check if the form is valid
        if form.is_valid():
            # Save the form data to the database
            form.save()
              
            return redirect('home')
    else :
        form = ProfileForms()
        data = Profile.objects.all()

        return render(request, 'student/home.html', {'form': form , 'data' : data})