from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
def validate_pin_length(value):
    if len(str(value)) != 6:
        raise ValidationError("The pin Code Must be exactly 6 Digits")
    
# List of Indian states as choices
INDIAN_STATES = [
    ("AP", "Andhra Pradesh"),
    ("AR", "Arunachal Pradesh"),
    ("AS", "Assam"),
    ("BR", "Bihar"),
    ("CG", "Chhattisgarh"),
    ("GA", "Goa"),
    ("GJ", "Gujarat"),
    ("HR", "Haryana"),
    ("HP", "Himachal Pradesh"),
    ("JK", "Jammu & Kashmir"),
    ("JH", "Jharkhand"),
    ("KA", "Karnataka"),
    ("KL", "Kerala"),
    ("MP", "Madhya Pradesh"),
    ("MH", "Maharashtra"),
    ("MN", "Manipur"),
    ("ML", "Meghalaya"),
    ("MZ", "Mizoram"),
    ("NL", "Nagaland"),
    ("OD", "Odisha"),
    ("PB", "Punjab"),
    ("RJ", "Rajasthan"),
    ("SK", "Sikkim"),
    ("TN", "Tamil Nadu"),
    ("TS", "Telangana"),
    ("TR", "Tripura"),
    ("UP", "Uttar Pradesh"),
    ("UK", "Uttarakhand"),
    ("WB", "West Bengal"),
    ("AN", "Andaman & Nicobar Islands"),
    ("CH", "Chandigarh"),
    ("DN", "Dadra & Nagar Haveli"),
    ("DD", "Daman & Diu"),
    ("LD", "Lakshadweep"),
    ("DL", "Delhi"),
    ("PY", "Puducherry"),
]


# Create your models here.
class Profile (models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False , auto_now_add=False)
    gender = models.CharField(max_length=1)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField(help_text='Enter 6 digit pin code' , validators=[validate_pin_length])
    state = models.CharField(
            max_length=2,
            choices=INDIAN_STATES,
            help_text="Select your state",
        )
    mobile = models.CharField(max_length=10 , help_text='Enter 10 digit mobile number' , validators=[RegexValidator(regex = r'^\d{10}$')] )
    email = models.EmailField()
    job_city = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profileimage', blank=True)
    my_file = models.FileField(upload_to='doc' , blank=True)