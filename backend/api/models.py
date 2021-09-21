from django.db import models

def nameFile(instance, filename):
    return '/'.join([filename])

class Party_Contact(models.Model):
    name = models.CharField(null=True, blank=False, max_length=60)
    email = models.CharField(null=True, blank=False, max_length=100)
    phone = models.IntegerField(null=True, blank=False)
    city = models.CharField(null=True, blank=True, max_length=24)
    state = models.CharField(null=True, blank=True, max_length=24)

    def __str__(self):
        return str(self.name)

class Policy_Position(models.Model):
    position_name = models.CharField(null=True, blank=False, max_length=60)
    description = models.TextField(null=True, blank=True, max_length=260)

    def __str__(self):
        return str(self.position_name)

class News_Letter(models.Model):
    author = models.CharField(null=True, blank=True, max_length=50)
    body = models.TextField(null=True, blank=False, max_length=3000)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.created_on)

class Meet_Member(models.Model):
    name = models.CharField(null=True, blank=False, max_length=60)
    position = models.CharField(null=True, blank=False, max_length=60),
    image = models.ImageField(null=True, blank=True, upload_to=nameFile)
    about = models.TextField(null=True, blank=True, max_length=2000)

    def __str__(self):
        return str(self.name)

class Home(models.Model):
    banner = models.ImageField(null=True, blank=True, upload_to=nameFile)
    logo = models.ImageField(null=True, blank=True, upload_to=nameFile)
    video = models.URLField(null=True, blank=True)

    def getBanner(self):
        return str(self.banner)

    def getLogo(self):
        return str(self.logo)

class Contact(models.Model):
    name = models.CharField(null=True, blank=False,max_length=50)
    email = models.CharField(null=True, blank=False, max_length=100)
    phone = models.IntegerField(null=True, blank=True)
    message = models.CharField(null=True, blank=True,max_length=350)
    created_on = models.DateField(auto_now_add=True)
  
    def __str__(self):
        return str(self.name)

class About(models.Model):
    description = models.TextField(null=True,blank=False,max_length=3000)

    def __str__(self):
        return str(self.description)

    
class Archive(models.Model):
    author = models.CharField(null=True, blank=True, max_length=50)
    body = models.TextField(null=True, blank=True, max_length=3000)
    banner = models.ImageField(null=True, blank=True, upload_to=nameFile)
    logo = models.ImageField(null=True, blank=True, upload_to=nameFile)
    video = models.URLField(null=True, blank=True)
    created_on = models.DateField(auto_now_add=True)
