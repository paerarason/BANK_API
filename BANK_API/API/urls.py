from django.urls import path,include
from . import views
urlpatterns=[
    path('branch/',views.branch),
    path('bank/',views.bank),
    path('branch/<str:location>/',views.select,name="branch_code"),
    path('bank/<str:pk>/',views.by_ifsc,name="ifsc_code")
]