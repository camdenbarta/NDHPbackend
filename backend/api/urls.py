from . import views
from rest_framework import routers
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()
router.register(r'party', views.Party_Contact_List)
router.register(r'position', views.Policy_Position_List)
router.register(r'letter', views.News_Letter_List)
router.register(r'member', views.Meet_Member_List)
router.register(r'image-video', views.Image_Video_List)
router.register(r'contact', views.Contact_List)
router.register(r'about', views.About_List)
router.register(r'records', views.Archive_List)

urlpatterns = [ 
    path('', include(router.urls)),
    path(r'emailcontact', views.emailContact, name='emailcontact'),
    #path(r'about1',views.about1, name='about1'),
    #path(r'about2',views.about2, name='about2'),
    #path(r'about3',views.about3, name='about3'),
    #path(r'about4',views.about4, name='about4'),
    #path(r'about5',views.about5, name='about5'),
    #path(r'about6',views.about6, name='about6'),
]
urlpatterns += staticfiles_urlpatterns()