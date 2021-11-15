from .models import About, Carousel, Contact, Image, Meet_Member, News_Letter, Policy_Position, PreSet, Video
from rest_framework import serializers

class PreSet_Serializer(serializers.ModelSerializer):
    class Meta:
        model = PreSet
        fields = ['order_no', 'created_at', 'updated_at']

class Policy_Position_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Policy_Position
        fields = ['order_no','position_name', 'description', 'bullet1', 'bullet2', 'bullet3', 'bullet4', 'created_at', 'updated_at']

class News_Letter_Serializer(serializers.ModelSerializer):
    class Meta:
        model = News_Letter
        fields = ['order_no','title', 'author','body1','body2','body3','body4','body5','bullet1','bullet2','bullet3','bullet4','bullet5', 'created_at', 'updated_at', 'getDate', 'getYear']

class Meet_Member_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Meet_Member
        fields = ['order_no','name', 'title', 'image', 'about', 'created_at', 'updated_at']

class Image_Serializer(serializers.ModelSerializer):
    location = serializers.StringRelatedField(many=False)
    class Meta:
        model = Image
        fields = ['location', 'title', 'image', 'created_at', 'updated_at']

class Video_Serializer(serializers.ModelSerializer):
    location = serializers.StringRelatedField(many=False)
    class Meta:
        model = Video
        fields = ['location', 'title', 'video_URL', 'created_at', 'updated_at']

class Contact_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['first_name','last_name','email', 'phone', 'message', 'created_at']

class About_Serializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['order_no','title','paragraph', 'bullet', 'created_at', 'updated_at']

class Carousel_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Carousel
        fields = ['imageName', 'image', 'created_at']