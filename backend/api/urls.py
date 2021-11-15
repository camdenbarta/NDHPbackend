from . import views
from rest_framework import routers
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()
router.register(r'position', views.Policy_Position_List)
router.register(r'letter', views.News_Letter_List)
router.register(r'member', views.Meet_Member_List)
router.register(r'img', views.Image_List)
router.register(r'vd', views.Video_List)
router.register(r'contact', views.Contact_List)
router.register(r'about', views.About_List)
router.register(r'carousel', views.Carousel_List)

urlpatterns = [ 
    path('', include(router.urls)),
    path(r'emailcontact', views.emailContact, name='emailcontact'),
]
urlpatterns += staticfiles_urlpatterns()