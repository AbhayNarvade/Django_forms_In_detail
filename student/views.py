from django.shortcuts import render , redirect , get_object_or_404
from .models import Profile
from .forms import ProfileForms
from django.http import HttpResponse 
import os
from django.db import models
from django.conf import settings


# Create your views here.
def home(request):
    if request.method == "POST":
        # Initialize the form with POST data and files
        try :
            form = ProfileForms(request.POST, request.FILES)
            
            # Check if the form is valid
            if form.is_valid():
                # Save the form data to the database
                form.save()
                
                return redirect('home')
        except Exception as e :
            return HttpResponse(f"The Error is encounter {e}")
    
    else :
        form = ProfileForms()
        data = Profile.objects.all()

        return render(request, 'student/home.html', {'form': form , 'data' : data})
    


def deletedata(request, pk):
    # Fetch the profile using the primary key (pk)
    data = get_object_or_404(Profile, pk=pk)

    if data:
        alldata = []
        # Loop through the model fields and collect the field names and their corresponding values
        for field in data._meta.fields:
            field_name = field.name
            field_value = getattr(data, field_name)

            # Handle file fields (FileField/ImageField)
            if isinstance(field, (models.FileField, models.ImageField)) and field_value:
                # For FileField or ImageField, show the file URL
                file_url = field_value.url if hasattr(field_value, 'url') else None
                alldata.append((field_name, file_url))  # Appending the file URL

        
        for value in alldata:
            file_name = value[1]
            print(f"file_name: {file_name}")
            # Construct the file path relative to BASE_DIR
            filepath = str(settings.MEDIA_ROOT) + "" +  file_name
            if os.path.exists(filepath):
                os.unlink(filepath) 
                # print('exit')

        data.delete()

        # return HttpResponse(alldata)
            

    # Now delete the data (profile)
    # data.delete()

    # Redirect to the home page
    return redirect('home')


def update(request, pk):
    # Fetch the profile using the primary key (pk)
    profile = get_object_or_404(Profile, pk=pk)
    
    # Initialize the form with the profile data if it's a GET request
    if request.method == 'GET':
        form = ProfileForms(instance=profile)
    else:
        form = ProfileForms(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            # Redirect after successful form submission
            return redirect('success_url')  # Update with your redirect URL

    # Return the form with the existing profile data
    return render(request, 'student/update.html', {'form': form, 'data': profile})