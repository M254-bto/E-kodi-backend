from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import LandlordSerializer, ProfileSerializer, AppartmentsSerializer
from .models import Landlord, Profile, Appartments
import random, string
from rest_framework.authtoken.models import Token




@api_view(['GET'])
@permission_classes([AllowAny])
def landlords(request):
    user = LandlordSerializer(Landlord.objects.all(), many=True).data
    return Response(user, status=status.HTTP_200_OK)
    




@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([TokenAuthentication])
def register(request):
    user = LandlordSerializer(data=request.data)
    if user.is_valid():
        new_user = Landlord.objects.create_user(**user.validated_data)
        return Response(user.data, status=status.HTTP_201_CREATED)
    return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def create_profile(request):
    prof = ProfileSerializer(data=request.data)
    if prof.is_valid():
        print('is_valid')
        Profile.objects.create(**prof.validated_data)
        return Response(prof.data, status=status.HTTP_201_CREATED)
    return Response(prof.errors, status=status.HTTP_400_BAD_REQUEST)





##Appartments API Views ##



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def create_appartment(request):
    user = Landlord.objects.get(id=request.user.id)
    app = AppartmentsSerializer(data=request.data)
    if app.is_valid():
        Appartments.objects.create(landlord=user, **app.validated_data)
        return Response(app.data, status=status.HTTP_201_CREATED)
    return Response(app.errors, status=status.HTTP_400_BAD_REQUEST)



## Appartment List ##

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([TokenAuthentication])
def appartments(request):
    app = AppartmentsSerializer(Appartments.objects.all(), many=True).data
    return Response(app, status=status.HTTP_200_OK)


@api_view(['GET'])
def appartments_by_landlord(request):
    user = request.user
    app = AppartmentsSerializer(Appartments.objects.filter(landlord=user), many=True).data
    return Response(app, status=status.HTTP_200_OK)


#appartment by id ##
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def appartment_by_id(request, pk):
    app = AppartmentsSerializer(Appartments.objects.get(id=pk)).data
    return Response(app, status=status.HTTP_200_OK)


#update appartment ##
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def update_appartment(request, pk):
    app = AppartmentsSerializer(Appartments.objects.get(id=pk), data=request.data)
    if app.is_valid():
        app.save()
        return Response(app.data, status=status.HTTP_200_OK)
    return Response(app.errors, status=status.HTTP_400_BAD_REQUEST)


#delete appartment ##
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def delete_appartment(request, pk):
    app = Appartments.objects.get(id=pk)
    app.delete()
    return Response(status=status.HTTP_204_NO_CONTENT) 
