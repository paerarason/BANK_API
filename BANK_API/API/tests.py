from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from .json import BankSeralizer,branch,bankbranch
# Create your tests here.
from .models import Branch
from . import views
import json
import requests
class TEST(APITestCase):
	def test_API_bank(self):
		url=reverse('ifsc_code',kwargs={'pk':'ABHY0065017'})
		headers={"Content-Type":"application/json"}
		con=requests.get('http://127.0.0.1:8000/api/bank/ABHY0065017/',headers=headers)
		self.assertEqual(con.status_code, status.HTTP_200_OK)
	def test_branch(self):
		data=[{
        "ifsc": "ANDB0002390",
        "address": "NO 7 8 A,PLOT NO 125 A3,3RD MAIN ROAD,NEW COLONY,CHROMPET,CHENNAI,600044",
        "city": "KANCHIPURAM",
        "state": "TAMIL NADU",
        "district": "KANCHEEPURAM",
        "bank": {
            "bank_id": 15,
            "bank_name": "ANDHRA BANK"
        },
        "branch": "CHROMPET"
    },
    {
        "ifsc": "BKID0008237",
        "address": "7, CLC WORKS ROAD, CHROMPET",
        "city": "CHENNAI",
        "state": "TAMIL NADU",
        "district": "CHENNAI",
        "bank": {
            "bank_id": 6,
            "bank_name": "BANK OF INDIA"
        },
        "branch": "CHROMPET"
    },
    {
        "ifsc": "CIUB0000150",
        "address": "NO 77 STATION ROAD  I FLOOR",
        "city": "CHENNAI",
        "state": "TAMIL NADU",
        "district": "CHENNAI",
        "bank": {
            "bank_id": 44,
            "bank_name": "CITY UNION BANK LIMITED"
        },
        "branch": "CHROMPET"
    },
    {
        "ifsc": "CIUB0000432",
        "address": "1 25, BASKAR PLAZA SIXTH MAIN ROAD, NEW COLONY, CHROMPET CHENNAI 600044 KANCHEEPURAM DIST",
        "city": "CHENNAI",
        "state": "TAMIL NADU",
        "district": "KANCHEEPURAM",
        "bank": {
            "bank_id": 44,
            "bank_name": "CITY UNION BANK LIMITED"
        },
        "branch": "NEW COLONY CHROMPET"
    },
    {
        "ifsc": "CNRB0001835",
        "address": "50, GROUND FLOOR,, RADHANAGAR MAIN ROAD,CHROMPET, CHENNAI 600 044.",
        "city": "CHENNAI",
        "state": "TAMIL NADU",
        "district": "CHENNAI",
        "bank": {
            "bank_id": 3,
            "bank_name": "CANARA BANK"
        },
        "branch": "RADHANAGAR CHROMPET CHENNAI"
    },
    {
        "ifsc": "IDIB000C028",
        "address": "10, BHASHYAM STREET, RADHA NAGAR, CHROMPET, CHENNAI 600044",
        "city": "PALLAVARAM",
        "state": "TAMIL NADU",
        "district": "KANCHEEPURAM",
        "bank": {
            "bank_id": 18,
            "bank_name": "INDIAN BANK"
        },
        "branch": "CHROMPET"
    },
    {
        "ifsc": "IOBA0001641",
        "address": "7  C L C WORKS ROAD  NEW COLONY, CHROMPET, CHENNAI 600044",
        "city": "CHENNAI",
        "state": "TAMIL NADU",
        "district": "CHENNAI",
        "bank": {
            "bank_id": 12,
            "bank_name": "INDIAN OVERSEAS BANK"
        },
        "branch": "CHROMPET"
    },
    {
        "ifsc": "LAVB0000211",
        "address": "PLOT NO 17,CLC WORKS ROAD, NAGAPPA NAGAR,CHROMPET,CHENNAI-600044",
        "city": "CHENNAI",
        "state": "TAMIL NADU",
        "district": "CHENNAI",
        "bank": {
            "bank_id": 49,
            "bank_name": "LAXMI VILAS BANK"
        },
        "branch": "CHROMPET"
    },
    {
        "ifsc": "PUNB0492000",
        "address": "7, CLC WORKS ROAD,CHROMPET,",
        "city": "CHENNAI",
        "state": "TAMIL NADU",
        "district": "CHENNAI",
        "bank": {
            "bank_id": 2,
            "bank_name": "PUNJAB NATIONAL BANK"
        },
        "branch": "CHROMPET CHENNAI"
    },
    {
        "ifsc": "SBMY0040989",
        "address": "NO 108 SHANTHI NAGAR CHROMPET CHENNAI",
        "city": "CHENNAI",
        "state": "TAMIL NADU",
        "district": "CHENNAI",
        "bank": {
            "bank_id": 31,
            "bank_name": "STATE BANK OF MYSORE"
        },
        "branch": "CHROMPET"
    }
]

		headers={"Content-Type":"application/json"}
		con=requests.get('http://127.0.0.1:8000/api/branch/chrompet',headers=headers)
		self.assertEqual(con.status_code, status.HTTP_200_OK)
		self.assertEqual(con.json(),data)