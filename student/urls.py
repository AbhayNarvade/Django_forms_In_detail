from django.urls import path
from .views import * 
urlpatterns = [
    path('', home , name='home'),
    path('<int:pk>/', deletedata , name='Delete'),
    path('<int:pk>/update/', update , name='update'),
]
