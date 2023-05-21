from django.db import models

class Closet(models.Model):
    #image = models.ImageField(upload_to = "images/", null=True, blank=True)
    imgfile = models.ImageField(null=True, upload_to="", blank=True) # 이미지 컬럼 추가
    classification = models.CharField(max_length=100, null=True,default='')

    #def __str__(self):
        #return self.classification
# Create your models here.
