from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from app_gmk_staff.models import StaffRegister

from app_gmk_staff.serializers import StaffRegisterSerializer

# Create your views here.

@csrf_exempt
def CURDStaffRegisterApi(request, pk=""):
    # try:
        if request.method == 'GET':
            if not pk:
                staffRegister = StaffRegister.objects.all()
                staffRegisterSerializer = StaffRegisterSerializer(
                    staffRegister, many=True)
                # return JsonResponse(request.method, safe=False)
                return JsonResponse(staffRegisterSerializer.data, safe=False)
            else:
                staffRegister = StaffRegister.objects.get(
                    StaffRegisterId=pk)
                staffRegisterSerializer = StaffRegisterSerializer(
                    staffRegister)
                return JsonResponse(staffRegisterSerializer.data, safe=False)
        elif request.method == 'POST':
            staffRegisterData = JSONParser().parse(request)
            # return JsonResponse(staffRegisterData, safe=False)
            staffRegisterSerializer = StaffRegisterSerializer(
                data=staffRegisterData)
            if staffRegisterSerializer.is_valid():
                staffRegisterSerializer.save()
                return JsonResponse(staffRegisterSerializer.data['StaffRegisterId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            staffRegisterData = JSONParser().parse(request)
            staffRegister = StaffRegister.objects.get(
                StaffRegisterId=staffRegisterData['StaffRegisterId'])
            staffRegisterSerializer = StaffRegisterSerializer(
                staffRegister, data=staffRegisterData)
            if staffRegisterSerializer.is_valid():
                staffRegisterSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            staffRegister = StaffRegister.objects.get(StaffRegisterId=pk)
            staffRegister.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)
