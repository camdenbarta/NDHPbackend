from .models import About, Archive, Contact, Image_Video, Meet_Member, News_Letter, Party_Contact, Policy_Position, PreSet
from rest_framework import serializers

class PreSet_Serializer(serializers.ModelSerializer):
    class Meta:
        model = PreSet
        fields = ['order_no', 'created_at', 'updated_at']

class Party_Contact_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Party_Contact
        fields = ['order_no','name','email','phone','city', 'state']

class Policy_Position_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Policy_Position
        fields = ['order_no','position_name', 'description', 'bullet1', 'bullet2', 'bullet3', 'bullet4']

class News_Letter_Serializer(serializers.ModelSerializer):
    class Meta:
        model = News_Letter
        fields = ['order_no','title', 'author','body1','body2','body3','body4','body5','bullet1','bullet2','bullet3','bullet4','bullet5']

class Meet_Member_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Meet_Member
        fields = ['order_no','name', 'title', 'image', 'about']

class Image_Video_Serializer(serializers.ModelSerializer):
    location = serializers.StringRelatedField(many=False)
    class Meta:
        model = Image_Video
        fields = ['location', 'title', 'image', 'video_URL']

class Contact_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['first_name','last_name','email', 'phone', 'message']

class About_Serializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['order_no','title','paragraph', 'bullet']

class Archive_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Archive
        fields = ['order_no','author', 'body', 'banner', 'logo', 'video', 'created_on']