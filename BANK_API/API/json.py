from rest_framework import serializers
from .models import Banks,Branch

class BankSeralizer(serializers.ModelSerializer):
    class Meta:
        model =Banks
        fields =['bank_id','bank_name']

class branch(serializers.ModelSerializer):
     bank=BankSeralizer
     class Meta:
        model =Branch
        fields =['ifsc','address','city','state','district','bank']
        depth=1

class bankbranch(serializers.ModelSerializer):
     bank_id=serializers.IntegerField(write_only=True)
     bank=BankSeralizer(read_only=True)
     class Meta:
        model =Branch
        fields =['ifsc','address','city','state','district','bank','branch',"bank_id"]
        depth=1