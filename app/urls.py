from django.urls import path
from.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('video/', video, name='video'),
    path('video/<int:video_id>/', video_detail, name='video_detail'), 
    path('upload/', upload_video, name='upload_video'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)