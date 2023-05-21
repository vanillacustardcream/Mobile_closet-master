from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('closet/', views.closet, name = 'closet'),
    path('closet/upload/', views.img_upload, name = 'img_upload'),
    path('closet/predict/', views.predict, name = 'predict'),
    path('closet/results/', views.view_results, name='results'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # media 경로 추가