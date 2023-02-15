from rest_framework import serializers
from .models import *


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('__all__')


class Input_OutputSerializer(serializers.ModelSerializer):
    account = AccountSerializer(required=False)
    account_id = serializers.IntegerField(required=False)

    class Meta:
        model = Input_Output
        fields = ('__all__')