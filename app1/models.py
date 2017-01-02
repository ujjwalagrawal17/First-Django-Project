from __future__ import unicode_literals

from django.db import models

# Create your models here.

class image_data(models.Model):
   	created= models.DateTimeField(auto_now=False,auto_now_add=True)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)	
	show=models.BooleanField(default=False)
	image=models.ImageField(upload_to='/media/images_pi/,default="/media/images_pi/default.png"')