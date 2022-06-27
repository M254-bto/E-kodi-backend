from django.urls import path, include
from .views import create_profile, register, landlords, appartments_by_landlord, appartments, create_appartment, appartment_by_id



from django.contrib.auth.models import User

urlpatterns = [
path('', landlords, name='landlords'),
path('auth/', include('landlord.authurls')),
path('register/', register, name='register'),
path('profile/create/', create_profile, name='create_profile'),
path('appartments/', appartments, name='appartments'),
path('appartments/me/new/', create_appartment, name='create_appartment'),
path('appartments/me/', appartments_by_landlord, name='appartments_by_landlord'),
path('appartments/me/<int:pk>/', appartment_by_id, name='appartment_by_id'),
]