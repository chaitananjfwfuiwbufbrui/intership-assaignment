from django.shortcuts import render
import json
from django.shortcuts import render
from .models import  *
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.shortcuts import  render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import  api_view, permission_classes
from .serializers import *
from rest_framework.response import Response


@csrf_exempt
@api_view(['POST','GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def superuser(request):
    if request.method == "GET":
        # jsondat = request.body
        # stram = io.BytesIO(jsondat)
        # data = JSONParser().parse(stram)


        
        us = UserAccount.objects.filter(email=request.user).first()
        us.is_staff = True
        us.is_superuser = True
        us.save()
        print(us.is_staff)
        message = {"message":"super user created"}
        return  JsonResponse(message,safe=False,status=200)

        
@csrf_exempt
@api_view(['POST','GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def Advisor(request):
    if request.method == "POST":
        try :
            jsondat = request.body
            stram = io.BytesIO(jsondat)
            python_data = JSONParser().parse(stram)
            Advisor_name = python_data['Advisor_name']
            Advisor_Photo_URL = python_data['Advisor_Photo_URL']


            if request.user.is_authenticated:
               
                queryset = advisor.objects.get_or_create(advisor=request.user,advisor_name=Advisor_name,image_urls=Advisor_Photo_URL)
                
                message = {"message":"Advisor account user created"}
                return  JsonResponse(message,safe=False,status=200)
            else:
                message = {"message":"please login"}
                return  JsonResponse(message,safe=False,status=200)
        except:
            message = {"message":"above fields missing"}
            return  JsonResponse(message,safe=False,status=400)



@csrf_exempt
@api_view(['POST','GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def home(request,id,advisorid=None):
    if request.method == "GET":
        
        all_advisors = advisor.objects.all()
        avicer_seralizer = AdvisorSerializer(all_advisors,many=True)


        
        return  JsonResponse(avicer_seralizer.data,safe=False,status=200)
 
    if request.method == "POST":
        jsondat = request.body
        stram = io.BytesIO(jsondat)
        python_data = JSONParser().parse(stram)
        
        selected_advisors = advisor.objects.get(id=advisorid)
        booking = Booking_call.objects.create(customer = request.user,Adviser=selected_advisors,Booking_time = python_data['booking_time'])
        


        message = {"message":"above fields missing"}
        return  JsonResponse(message,safe=False,status=400)



@csrf_exempt
@api_view(['POST','GET','PUT','DELETE'])
@permission_classes([AllowAny])
def booking(request,id):
    if request.method == "GET":
        print(request.user)
        if request.user.is_authenticated:
            
        
            all_booking = Booking_call.objects.filter(customer=request.user)
            avicer_seralizer = BookingSerializer(all_booking,many=True)
          
        
            return  JsonResponse(avicer_seralizer.data,safe=False,status=200)
        