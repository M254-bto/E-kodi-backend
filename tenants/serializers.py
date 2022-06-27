from rest_framework.serializers import ModelSerializer
from .models import Tenant


class TenantSerializer(ModelSerializer):
    class Meta:
        model = Tenant
        fields = ['id','appartment','username', 'first_name', 'last_name','contact', 'email']



