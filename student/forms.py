from .models import Profile
from django import forms

GENDER_CHOICES = (
    ('M','Male'),
    ('F','Female'),
    ('O','Other'),
)

JOB_CITIES = [
    ("Mumbai", "Mumbai"),
    ("Delhi", "Delhi"),
    ("Bangalore", "Bangalore"),
    ("Hyderabad", "Hyderabad"),
    ("Ahmedabad", "Ahmedabad"),
    ("Chennai", "Chennai"),
    ("Kolkata", "Kolkata"),
    ("Pune", "Pune"),
    ("Jaipur", "Jaipur"),
    ("Lucknow", "Lucknow"),
]


class ProfileForms(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES , widget= forms.RadioSelect )
    
    class Meta :
        model = Profile
        fields = [
            "name","dob","gender","locality","city","pin","state","mobile","email","job_city","profile_image","my_file",
        ]

        labels = {
            'name' : 'Full Name',
            'pin' : 'Pin Code',
            'mobile' : 'Mobile Number',
            'dob' : 'Date of Birth',
            'job_city' : 'Prefered job city'
        }

        help_texts = {
         'profile_image': 'Upload your profile photo',
         'my_file' : 'optional : Attach any additional document (PDF , DOCX , etc.) ',
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}) , 
            'dob' : forms.TextInput(attrs={'class' : 'form-control' , 'type' : 'date'}) ,
            'locality' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'write your area name'}) ,
            'city' : forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'write your city name'}) ,
            'pin' : forms.NumberInput(attrs={'class' : 'form-control' , 'placeholder' : 'Enter your Pin code', }) ,
            'state' : forms.Select(attrs={'class' : 'form-select'  }) ,
            'mobile' : forms.NumberInput(attrs={'class' : 'form-control' , 'placeholder' : 'Enter your mobile number', }) ,
            'email' : forms.EmailInput(attrs={'class' : 'form-control' , 'placeholder' : 'Enter your email', }) ,
            'job_city' : forms.CheckboxSelectMultiple(attrs={'class' : 'form-check-input' } , choices= JOB_CITIES) ,
            'profile_image' : forms.FileInput(attrs={'class' : 'form-control' , } ) ,
            'my_file' : forms.FileInput(attrs={'class' : 'form-control' ,  } ) ,
        }

