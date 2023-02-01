from django.shortcuts import render,HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.decorators import api_view
from django.contrib.auth.models import User,Group
from .models import Banks,Branch
import requests
from .json import BankSeralizer,branch,bankbranch
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
import pandas as pd
from .decorater import capitalise
from django.db import Q
@api_view(["GET","POST"])
def branch(request):
  if request.method=="POST":
    instance=bankbranch(data=request.data)
    if instance.is_valid():
        bank=Banks.objects.get(bank_id=request.data['bank_id'])
        instance.bank=BankSeralizer(bank)
        instance.save()
        return Response(instance.data,status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)
    
  else:
    dat=Branch.objects.all()
    instance=bankbranch(dat,many=True)
    return Response(instance.data,status=status.HTTP_200_OK)


@api_view(["GET","POST"])
def bank(request):
 if request.method=="POST":
    instance=BankSeralizer(data=request.data)
    print(request.data)
    if instance.is_valid():
        instance.save()
        return Response(instance.data,status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)
 else:
    dat=Banks.objects.all()
    instance=BankSeralizer(dat,many=True)
    return Response(instance.data,status=status.HTTP_200_OK)
@capitalise
@api_view(["GET"])
def select(request,location):
    branch=Branch.objects.filter(Q(branch__icontains=location) | Q(address__icontains=location)).order_by('ifsc').values()
    if branch.count()>0:
        instance=bankbranch(branch,many=True)
        return Response(instance.data,status=status.HTTP_200_OK)
    return HttpResponse(status=404)
    

@api_view(["GET"])
def by_ifsc(request,pk): 

    try:
        snippet=Branch.objects.get(ifsc=pk)
    except Branch.DoesNotExist:
        return HttpResponse(status=404)
    instance=bankbranch(snippet)
    return Response(instance.data,status=status.HTTP_200_OK)
      
    