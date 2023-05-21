from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Closet

import pandas as pd
from keras.preprocessing import image
import numpy as np
from keras.applications.vgg16 import preprocess_input
from keras.applications.imagenet_utils import decode_predictions
from keras.applications.imagenet_utils import preprocess_input

def closet(request):
    closets = Closet.objects.all()
    return render(request, 'closet.html', {'closets': closets })

def img_upload(request):
    if(request.method == 'POST'):
        closet = Closet()
        closet.imgfile = request.FILES['imgfile']
        
        closet.save()
        return redirect('/closet')

    else:
        print('실패')
        return render(request, 'upload.html')  
    
def predict(request):
    #pass
    if request.POST.get('action') == 'post':

        img =  request.FILES['imgfile']

        model = pd.read_pickle(r"C:\Users\kshsj\Desktop\뱁새\new_model.pkl")

        target_size = 224
        img = img.resize((target_size, target_size))

        np_img = image.img_to_array(img)
        img_batch = np.expand_dims(np_img, axis=0)

        pre_processed = preprocess_input(img_batch)

        y_preds = model.predict(pre_processed)
 
        np.set_printoptions(suppress=True, precision=10)

        classification = decode_predictions(y_preds, top=1)

        Closet.objects.create(classification=classification)

        return JsonResponse({'result' : classification}, safe=False)

def view_results(request):
    return render(request, "result.html")     

# Create your views here.
