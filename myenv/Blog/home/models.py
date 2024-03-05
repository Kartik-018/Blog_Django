from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import *
# Create your models here.
class BlogModel(models.Model):
    tittle=models.CharField(max_length=1000)
    content=FroalaField()
    slug=models.SlugField(max_length=1000,null=True,blank=True)
    image=models.ImageField(upload_to='blog')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tittle
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.tittle)
        super(BlogModel,self).save(*args,**kwargs)


    