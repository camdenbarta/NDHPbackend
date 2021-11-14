from rest_framework.response import Response
from backend.settings import EMAIL_HOST_USER, SEND_EMAIL_USER
from django.http.response import HttpResponse
from .serializers import About_Serializer, Archive_Serializer, Carousel_Serializer, Contact_Serializer, Image_Video_Serializer, Meet_Member_Serializer, News_Letter_Serializer, Party_Contact_Serializer, Policy_Position_Serializer
from .models import About, Archive, Carousel, Contact, Image_Video, Meet_Member, News_Letter, Order_On_Page, Party_Contact, Policy_Position
from rest_framework import serializers, viewsets
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

class Party_Contact_List(viewsets.ModelViewSet):
   queryset = Party_Contact.objects.all()
   serializer_class = Party_Contact_Serializer

   def get(self, request):
        return HttpResponse(self.queryset)

class Policy_Position_List(viewsets.ModelViewSet):
   queryset = Policy_Position.objects.all()
   serializer_class = Policy_Position_Serializer

   def get(self, request):
          return HttpResponse(self.queryset)

class News_Letter_List(viewsets.ModelViewSet):
   queryset = News_Letter.objects.all()
   serializer_class = News_Letter_Serializer

   def get(self, request):
        return HttpResponse(self.queryset)

class Meet_Member_List(viewsets.ModelViewSet):
    queryset = Meet_Member.objects.all()
    serializer_class = Meet_Member_Serializer

    def get(self, request):
        return HttpResponse(self.queryset)

class Image_Video_List(viewsets.ModelViewSet):
    queryset = Image_Video.objects.all()
    serializer_class = Image_Video_Serializer

    def get(self, request):
        return HttpResponse(self.queryset)

class About_List(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = About_Serializer

    def get(self, request):
        return HttpResponse(self.queryset)

class Archive_List(viewsets.ModelViewSet):
    queryset = Archive.objects.all()
    serializer_class = Archive_Serializer

    def get(self, request):
        return HttpResponse(self.queryset)

class Carousel_List(viewsets.ModelViewSet):
    queryset = Carousel.objects.all()
    serializer_class = Carousel_Serializer

    def get(self, request):
        return HttpResponse(self.queryset)

class Contact_List(viewsets.ModelViewSet):
     queryset = Contact.objects.all()
     serializer_class = Contact_Serializer

     def post(self, request):
          return HttpResponse(self.queryset)

@csrf_exempt
def emailContact(request):
    if request.method =='POST':
            data = JSONParser().parse(request)          
            serializer = Contact_Serializer(data=data)
            if serializer.is_valid():
                for e in Contact.objects.all():
                    body = ("Contact Name: " + str(e.name) + "\n" + "Email: " + str(e.email) + "\n" + 
                    "Phone Number: " + str(e.phone) + "\n" + "Message: " + str(e.message))
                send_mail(
                    'Contact Form',
                    body,
                    EMAIL_HOST_USER,
                    [SEND_EMAIL_USER],
                    fail_silently=False
                )
    return HttpResponse(request)