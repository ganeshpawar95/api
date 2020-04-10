from django.urls import path,include
from .views import *
from django.conf import settings
from .views import RemovebgView,RemovebgEdit,RemovebgpostView,RemovebgDetails
from django.conf.urls.static import static

urlpatterns = [
    path('',removebg,name='removebg'),
    path('removebgs/',RemovebgView.as_view()),
     path('edit/<int:pk>',RemovebgEdit.as_view()),
    path('details/<int:pk>',RemovebgDetails.as_view()),
    path('add/', RemovebgpostView.as_view()),
   
    


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

