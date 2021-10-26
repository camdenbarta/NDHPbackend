from .models import About, Archive, Contact, Image_Video, Meet_Member, News_Letter, Party_Contact, Policy_Position
from rest_framework import serializers

class Party_Contact_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Party_Contact
        fields = ['name','email','phone','city', 'state']

class Policy_Position_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Policy_Position
        fields = ['position_name', 'description']

class News_Letter_Serializer(serializers.ModelSerializer):
    class Meta:
        model = News_Letter
        fields = ['author','body','created_on']

class Meet_Member_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Meet_Member
        fields = [ 'name', 'position', 'image', 'about']

class Image_Video_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Image_Video
        fields = ['banner', 'logo', 'video']

class Contact_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name','email', 'phone', 'message','created_on']

class About_Serializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['title','paragraph', 'bullet', 'updated']

class Archive_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Archive
        fields = ['author', 'body', 'banner', 'logo', 'video', 'created_on']