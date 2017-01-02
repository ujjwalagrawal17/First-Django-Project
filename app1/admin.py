from django.contrib import admin
from .models import *

# Register your models here.
class image_dataAdmin(admin.ModelAdmin):
	"""docstring for image_pi_dataAdmin"""
	list_display=["image","created","modified","show"]
admin.site.register(image_data,image_dataAdmin)