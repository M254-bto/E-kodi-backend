from rest_framework.serializers import ModelSerializer
from .models import Landlord, Profile, Appartments
from django.contrib.auth.models import User



class LandlordSerializer(ModelSerializer):
    class Meta:
        model = Landlord
        fields = ['username', 'first_name', 'last_name','contact', 'email']


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['image']




class AppartmentsSerializer(ModelSerializer):
    class Meta:
        model = Appartments
        fields = ['id','name', 'description', 'location', 'units', 'unit_price']