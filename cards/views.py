from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from cards.models import Course
from cards.serializers import CardSerializer

# Create your views here.

@csrf_exempt
def flashcardApi(request,id=0):
    if request.method=='GET':
        flash = Course.objects.all()
        flashSerializer=CardSerializer(flash,many=True)
        return JsonResponse(flashSerializer.data,safe=False)
    elif request.method=='POST':
        flash_data=JSONParser().parse(request)
        flashSerializer=CardSerializer(data=flash_data)
        if flashSerializer.is_valid():
            flashSerializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        flash_data=JSONParser().parse(request)
        flash=Course.objects.get(CourseId=flash_data['CourseId'])
        flashSerializer=CardSerializer(flash,data=flash_data)
        if flashSerializer.is_valid():
            flashSerializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        flash=Course.objects.get(CourseId=id)
        flash.delete()
        return JsonResponse("Deleted Successfully",safe=False)
        