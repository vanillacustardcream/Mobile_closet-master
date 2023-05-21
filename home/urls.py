from django.urls import path # path 함수를 이용하기 위해서 선언해줍니다.
from . import views     # from 옆에 .(점)은 현재 폴더(app)를 의미합니다. 즉 현재 폴더에 views.py를 가져옵니다


from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name = 'home'), 
    #path('likes/', views.like, name='like'),
    #path('like_ajax/',views.like_ajax, name='like_ajax'),
    #path('like/', views.likes, name="likes"),
    path('like/', views.likes, name="likes"),
    path('showlike/<int:user_id>', views.showlike, name='showlike'),
    #path('<int:pk>/', PhotoLikeView.as_view(), name='photo_like'),
    ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)    