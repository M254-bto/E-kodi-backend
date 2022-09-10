from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import TenantSerializer
from .models import Tenant
from landlord.models import Appartments
from .mpesa import MpesaAccessToken, LipanaMpesaPpassword
import requests



# tenants#
@api_view(['GET'])
@permission_classes([AllowAny])
def tenants(request):
    user = TenantSerializer(Tenant.objects.all(), many=True).data
    return Response(user, status=status.HTTP_200_OK)

# new tenant #
@api_view(['POST'])
def create_tenant(request):
    app = Appartments.objects.get(id=request.data['appartment'])
    if app.landlord.id == request.user.id:
        user = TenantSerializer(data=request.data)
        if user.is_valid():
            Tenant.objects.create_user(**user.validated_data)
            return Response(user.data, status=status.HTTP_201_CREATED)
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({"error":"You are not authorized"},status=status.HTTP_401_UNAUTHORIZED)


# tenant by appartment#
@api_view(['GET'])
def tenant_by_appartment(request, appartment_id):
    user = TenantSerializer(Tenant.objects.filter(appartment=appartment_id), many=True).data
    return Response(user, status=status.HTTP_200_OK)


# tenant by id#
@api_view(['GET'])
def tenant_by_id(request, tenant_id):
    user = TenantSerializer(Tenant.objects.get(id=tenant_id)).data
    return Response(user, status=status.HTTP_200_OK)

# update tenant#
@api_view(['PUT'])
def update_tenant(request, tenant_id):
    user = TenantSerializer(Tenant.objects.get(id=tenant_id), data=request.data)
    if user.is_valid():
        user.save()
        return Response(user.data, status=status.HTTP_200_OK)
    return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

    


#delete tenant#
@api_view(['DELETE'])
def delete_tenant(request, tenant_id):
    user = Tenant.objects.get(id=tenant_id)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


#tenants by landlord#
@api_view(['GET'])
def tenants_by_landlord(request):
    user = TenantSerializer(Tenant.objects.filter(appartment__landlord=request.user), many=True).data
    return Response(user, status=status.HTTP_200_OK)


#get tenant rent#
@api_view(['GET'])
def tenant_rent(request, tenant_id):
    rent = Tenant.objects.get(id=tenant_id).appartment.unit_price
    return Response(rent, status=status.HTTP_200_OK) 



#mpesa payment#
@api_view(['POST'])
def mpesa_payment(request, tenant_id):
    tenant = Tenant.objects.get(id=tenant_id)
    # phone_number = tenant.phone_number
    # amount = tenant.appartment.unit_price
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        # "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        # "Password": LipanaMpesaPpassword.decode_password,
        # "Timestamp": LipanaMpesaPpassword.lipa_time,
        # # "TransactionType": "CustomerPayBillOnline",
        # "Amount": 1,
        # # "PartyA": 254798159691,
        # # "PartyB": LipanaMpesaPpassword.Business_short_code,
        # "PhoneNumber": 254798159691,
        # "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
        # "AccountReference": f"{tenant}",
        # "TransactionDesc": "Testing stk push",
        "Command ID": "CustomerPayBillOnline",
        "Amount":1,
        "Msisdn": 254798159691,
        "BillRefNumber": 123456,
        "ShortCode":522522
 }

    response = requests.post(api_url, json=request, headers=headers)
    return Response(response.json(), status=status.HTTP_200_OK)