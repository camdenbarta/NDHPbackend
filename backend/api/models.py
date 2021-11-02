from django.db import models
from datetime import datetime
from django.utils import timezone

def nameFile(instance, filename):
    return '/'.join([filename])

class Order_On_Page(models.TextChoices):
    FIRST = "First", "First"
    SECOND = "Second", "Second"
    THIRD = "Third", "Third"
    FOURTH = "Fourth", "Fourth"
    FIFTH = "Fifth", "Fifth"
    SIXTH = "Sixth", "Sixth"

class Page(models.TextChoices):
    FIRST = 'About',"About"
    SECOND = 'Archive',"Archive"
    THIRD = 'Contact',"Contact"
    FOURTH = 'Home',"Home"
    FIFTH = 'Meet the Members',"Meet the Members"
    SIXTH = 'News Letter',"News Letter"

class Card(models.TextChoices):
    FIRST = 'Card 1',"Card 1"
    SECOND = 'Card 2',"Card 2"
    THIRD = 'Card 3',"Card 3"
    FOURTH = 'Card 4',"Card 4"
    FIFTH = 'Card 5',"Card 5"
    SIXTH = 'Card 6',"Card 6"

class PreSet(models.Model):
    #card_no = models.CharField(verbose_name='What Card the Info Goes In', max_length=8, default=Card.FIRST, choices=Card.choices)
    order_no = models.CharField(verbose_name='Location on Page', max_length=20, default=Order_On_Page.FIRST, choices=Order_On_Page.choices)
    dateTimeCompleted = models.DateField(verbose_name="Date Completed/Updated", null=True)

    class Meta:
        abstract = True

    def display(self):
        return str(" || " +"Page Order: "+str(self.order_no)+  " || " + "Updated: "+ str(self.dateTimeCompleted))

class Party_Contact(PreSet):
    name = models.CharField(verbose_name="Name of Member", null=True, blank=False, max_length=60)
    email = models.CharField(verbose_name="Member's Email", null=True, blank=False, max_length=100)
    position = models.CharField(verbose_name="Position Title (Optional)", null=True, blank=True, max_length=60)
    phone = models.CharField(verbose_name="Member's Phone Number (Optional)", null=True, blank=True, max_length=15)
    city = models.CharField(verbose_name="Member's Current City (Optional)", null=True, blank=True, max_length=24)
    state = models.CharField(verbose_name="Member's Current State (Optional)", null=True, blank=True, max_length=24)

    def __str__(self):
        return str(self.name + " || "+ self.email + self.display())

class Policy_Position(PreSet):
    position_name = models.CharField(verbose_name="Position Title", null=True, blank=False, max_length=60)
    description = models.TextField(verbose_name="Position Description (Optional)", null=True, blank=True, max_length=260)
    bullet = models.TextField(verbose_name="Position Bullet Points (Optional) --- This will be after all of the paragraphs *Enter one at a time", null=True, blank=True, max_length=260)

    class meta:
        verbose_name = "Policy Position"
        verbose_name_plural ="Policy Positions"

    def __str__(self):
        return str(self.position_name + self.display())

class News_Letter(PreSet):
    title = models.CharField(verbose_name="Title of the Article", null=True, blank=False, max_length=30)
    author = models.CharField(verbose_name="News Letter Author (Optional)", null=True, blank=True, max_length=50)
    body = models.TextField(verbose_name="News Letter body/ paragraph *Enter one paragraph at a time for page break", null=True, blank=False, max_length=3000)
    bullet = models.TextField(verbose_name="News Letter Bullet Points (Optional) --- This will be after all of the paragraphs *Enter one at a time", null=True, blank=True, max_length=260)

    def __str__(self):
        return str(self.title + self.display())

class Meet_Member(PreSet):
    name = models.CharField(null=True, blank=False, max_length=60)
    position = models.TextField(null=True, blank=False, max_length=50),
    image = models.ImageField(null=True, blank=True, upload_to=nameFile)
    about = models.TextField(null=True, blank=True, max_length=2000)

    def __str__(self):
        return str(self.name + self.display())

class Image_Video(PreSet):
    title = models.CharField(null=True, blank=False, max_length=50)
    location = models.CharField(verbose_name='Location in Website', max_length=20, default=Page.FOURTH, choices=Page.choices)
    image = models.ImageField(null=True, blank=True, upload_to=nameFile)
    video_URL = models.URLField(null=True, blank=True)

    def __str__(self):
        return str(self.title + " || Page: "+ str(self.location) + self.display())

class Contact(models.Model):
    name = models.CharField(null=True, blank=False,max_length=50)
    email = models.CharField(null=True, blank=False, max_length=100)
    phone = models.CharField(null=True, blank=True, max_length=15)
    message = models.CharField(null=True, blank=True,max_length=350)
  
    def __str__(self):
        return str(self.name)

class About(PreSet):
    title = models.CharField(null=True, blank=False, max_length=50)
    paragraph = models.TextField(null=True,blank=True,max_length=3000)
    bullet = models.TextField(null=True,blank=True,max_length=3000)


    def __str__(self):
        return str(self.title + self.display())
    
class Archive(PreSet):
    author = models.CharField(null=True, blank=True, max_length=50)
    body = models.TextField(null=True, blank=True, max_length=3000)
    banner = models.ImageField(null=True, blank=True, upload_to=nameFile)
    logo = models.ImageField(null=True, blank=True, upload_to=nameFile)
    video = models.URLField(null=True, blank=True)

    def __str__(self):
        return str(self.author + self.display())