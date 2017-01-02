from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@csrf_exempt
def get_images(request):
	response_data={}
	if request.method=='GET':
		try:

			image_list_data=image_data.objects.filter(show=True)
			for o in image_list_data:
			    response_data['image']=request.scheme+'://'+request.get_host()+'/media/'+str(o.image)
			response_data['success']=True
			response_data['message']='Successful'
		except Exception,e:
			print e
			response_data['success']=False
			response_data['message']='Error Occured'
	else:
		response_data['success']=False
		response_data['message']='You better get out of here'
	
	print JsonResponse(response_data)
	return JsonResponse(response_data)