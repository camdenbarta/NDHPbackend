from abc import ABC
from .models import About, Archive, Contact, Home, Meet_Member, News_Letter, Party_Contact, Policy_Position
from django.contrib import admin

admin.site.register(About)
admin.site.register(Archive)
admin.site.register(Contact)
admin.site.register(Home)
admin.site.register(Meet_Member)
admin.site.register(News_Letter)
admin.site.register(Party_Contact)
admin.site.register(Policy_Position)