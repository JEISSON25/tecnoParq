from django.shortcuts import render
from rest_framework import viewsets
from .models import Account, Input_Output
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import AccountSerializer, Input_OutputSerializer


class AccountViewset(viewsets.ModelViewSet):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ['=identify']
    ordering_fields = ('__all__')

class Input_OutputViewset(viewsets.ModelViewSet):

    queryset = Input_Output.objects.all()
    serializer_class = Input_OutputSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ['=account__identify', '=date_in']
    ordering_fields = ('__all__')
