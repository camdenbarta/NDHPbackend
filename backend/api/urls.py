from . import views
from rest_framework import routers
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()
router.register(r'party', views.Party_Contact_List)
router.register(r'position', views.Policy_Position_List)
router.register(r'letter', views.News_Letter_List)
router.register(r'member', views.Meet_Member_List)
router.register(r'home', views.Home_List)
router.register(r'contact', views.Contact_List)
router.register(r'about', views.About_List)
router.register(r'records', views.Archive_List)

urlpatterns = [ 
    path('', include(router.urls)),
    path('emailcontact/', views.emailContact, name='emailcontact'),
]
urlpatterns += staticfiles_urlpatterns()