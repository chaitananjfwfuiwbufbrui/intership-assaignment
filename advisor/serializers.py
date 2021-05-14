from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *

User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = advisor
        fields = ('advisor_name', 'image_urls')
class BookingSerializer(serializers.ModelSerializer):
    Adviser_name = serializers.CharField(read_only=True, source='Adviser.advisor_name')
    Adviser_image = serializers.CharField(read_only=True, source='Adviser.image_urls')
   
    class Meta:
        model = Booking_call
        fields = ('Adviser_name','Adviser_image','Adviser','Booking_time','id' )
    