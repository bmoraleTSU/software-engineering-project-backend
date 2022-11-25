from rest_framework import serializers
from .models import *

class AbcClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = AbcClient
        fields = [ 'abc_client_id',
                   'client_name',
                   'company_address',
                   'phone_number',
                   'created_by',
                   'created_date',
                   'modified_by',
                   'modified_date',
                   'is_deleted',
                ]
                
#Do same for other tables