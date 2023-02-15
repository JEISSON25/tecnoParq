from django.shortcuts import render
from rest_framework import viewsets
from .models import Account, Input_Output
from .serializers import AccountSerializer, Input_OutputSerializer
from django_filters import rest_framework as filters
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

class AccountViewset(viewsets.ModelViewSet):

    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    filter_backends = [
        filters.DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')
    ordering_fields = ('__all__')

class FiltroDate (filters.FilterSet):
    fecha_in = filters.DateFromToRangeFilter(field_name='date_in')
    account__id = filters.NumberFilter(field_name='account__id')

    class Meta:
        model: Input_Output
        fields = ['date_in', '=account__id']

class Input_OutputViewset(viewsets.ModelViewSet):

    queryset = Input_Output.objects.all()
    serializer_class = Input_OutputSerializer

    filter_backends = [
        filters.DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ['=account__identify', '=account__id', '=date_in']
    ordering_fields = ('__all__')
    filterset_class = FiltroDate
