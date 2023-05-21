from audioop import reverse
import warnings
from django.shortcuts import get_object_or_404, redirect, render
from .models import Photo
import json
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
# Create your views here.

def home(request):
    photos = Photo.objects.all()
    
    
    return render(request, 'home.html', {'photos': photos})

# def likes(request, pk):
#     photo = get_object_or_404(Photo, id=request.POST.get('photo_id'))
    

#     if photo.like.filter(id=request.user.id).exists():
#         photo.like.remove(request.user)
#     else :
#         photo.like.add(request.user)
#     return redirect("photo_like", args=[str(pk)]) 

# class PhotoLikeView(DetailView):
#     model = Photo

#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)

#         likes_connected = get_object_or_404(Photo, id=self.kwargs['pk'])
#         liked = False
#         if likes_connected.like.filter(id=self.request.user.id).exists():
#             liked = True
#         #data['number_of_likes'] = likes_connected.number_of_likes()
#         data['photo_is_liked'] = liked
#         return data

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def likes(request): 
    if is_ajax(request= request): #ajax 방식일 때 아래 코드 실행
        photo_id = request.GET['photo_id'] #좋아요를 누른 게시물id (photo_id)가지고 오기
        photo = Photo.objects.get(id=photo_id) 
				
        if not request.user.is_authenticated: #버튼을 누른 유저가 비로그인 유저일 때
            message = "로그인을 해주세요" #화면에 띄울 메세지 
            context = {"message":message}
            
            return HttpResponse(json.dumps(context), content_type='application/json' )

        user = request.user #request.user : 현재 로그인한 유저
        if photo.like.filter(id = user.id).exists(): #이미 좋아요를 누른 유저일 때
            photo.like.remove(user) #like field에 현재 유저 추가
            message = "좋아요 취소" #화면에 띄울 메세지
        else: #좋아요를 누르지 않은 유저일 때
            photo.like.add(user) #like field에 현재 유저 삭제
            message = "좋아요" #화면에 띄울 메세지
        
        context = {"message":message}
    return HttpResponse(json.dumps(context), content_type='application/json')
    
def showlike(request,user_id):  
    user = User.objects.get(id = user_id)
    photo_likes = user.likes.all()
    context={
        "photo_likes":photo_likes,
    }
    return render(request, 'like.html',context)

# @csrf_exempt 
# def like_ajax(request):
#     req = json.loads(request.body) 
#     photo_id = req['id'] 

#     photo = Photo.objects.get(id = photo_id)

#     if photo.already_like == True: #좋아요가 눌러져있으면
#         photo.already_like = False
#         status = photo.already_like
#         photo.like = '<i class="far fa-heart"></i> '
#         message = "좋아요 취소"
#     else: #좋아요가 안눌러져있으면
#         photo.already_like = True
#         status = photo.already_like
#         photo.like = ' <i class="fas fa-heart" style="color:red"></i>'
#         message = "좋아요"
#     photo.save()

#     return JsonResponse({'id': photo_id, 'message': message, 'status':status})

# @login_required
# @require_POST
# def like(request):
#     pk = request.POST.get('pk', None)
#     photo = get_object_or_404(Photo, pk=pk)
#     user = request.user

#     if photo.like.filter(id=user.id).exists():
#         photo.like.remove(user)
#         message = '좋아요 취소'
#     else:
#         photo.like.add(user)
#         message = '좋아요'

#     context = {'message ': message}
#     return HttpResponse(json.dumps(context), content_type="application/json")

# def likes(request, photo_id):
    
#     if request.user.is_authenticated:
#         photo = get_object_or_404(Photo, id = photo_id)

#         if photo.like_users.filter(pk=request.user.id).exists():
#             photo.like_users.remove(request.user)
#         else:
#             photo.like_users.add(request.user)
#         return redirect('home.html')
#     return redirect('accouts:login')

