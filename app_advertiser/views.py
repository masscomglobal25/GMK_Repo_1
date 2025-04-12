from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from app_advertiser.models import Profile

from app_advertiser.serializers import ProfileRegisterSerializer, ProfileSerializer, SaveProfileSerializer, UploadProfileSerializer

# Create your views here.


@csrf_exempt
def CURDAdvertiserProfileApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                profile = Profile.objects.all()
                profileSerializer = ProfileSerializer(
                    profile, many=True)
                return JsonResponse(profileSerializer.data, safe=False)
            else:
                profile = Profile.objects.get(
                    AdvertiserId=pk)
                profileSerializer = ProfileSerializer(
                    profile)
                return JsonResponse(profileSerializer.data, safe=False)
        elif request.method == 'POST':
            profileData = JSONParser().parse(request)
            # return JsonResponse(profileData, safe=False)
            profileSerializer = SaveProfileSerializer(
                data=profileData)
            if profileSerializer.is_valid():
                profileSerializer.save()
                return JsonResponse(profileSerializer.data['AdvertiserId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            profileData = JSONParser().parse(request)
            profile = Profile.objects.get(
                AdvertiserId=profileData['AdvertiserId'])
            profileSerializer = SaveProfileSerializer(
                profile, data=profileData)
            if profileSerializer.is_valid():
                profileSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            profile = Profile.objects.get(
                AdvertiserId=pk)
            Profile.objects.get(
                AdvertiserId=pk).ProfileImage.delete(save=True)
            profile.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("", safe=False)

@csrf_exempt
def GetCreditCount(request, pk=""):
    try:
        if request.method == 'GET':
            profile = Profile.objects.get(
                AdvertiserId=pk)
            profileSerializer = ProfileSerializer(
                profile)
            return JsonResponse(profileSerializer.data['Credits'], safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)

@csrf_exempt
def UpdateCreditCount(request):
    try:
        if request.method == 'POST':
            profileData = JSONParser().parse(request)
            profile = Profile.objects.get(
                AdvertiserId=profileData['AdvertiserId'])
            profileSerializer = ProfileSerializer(
                    profile)
            data=profileSerializer.data
            data['Credits']=int(data['Credits'])-int(profileData['RedeemCredits'])
            profileSerializer = SaveProfileSerializer(
                profile, data=data)
            if profileSerializer.is_valid():
                profileSerializer.save()
                return JsonResponse("Update successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)

@csrf_exempt
def CURDAdvertiserRegisterApi(request, pk=""):
    try:
        if request.method == 'POST':
            profileData = JSONParser().parse(request)
            # return JsonResponse(profileData, safe=False)
            profileSerializer = ProfileRegisterSerializer(
                data=profileData)
            if profileSerializer.is_valid():
                profileSerializer.save()
                return JsonResponse(profileSerializer.data['AdvertiserId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)

class UploadAdvertiserProfileFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, pk="", *args, **kwargs):
        # try:
            if not pk:
                file_serializer = UploadProfileSerializer(data=request.data)
                if file_serializer.is_valid():
                    file_serializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse("failed", safe=False)
            else:
                profile = Profile.objects.get(
                    AdvertiserId=pk)
                Profile.objects.get(
                    AdvertiserId=pk).ProfileImage.delete(save=True)
                uploadProfileSerializer = UploadProfileSerializer(
                    profile, data=request.data)
                if uploadProfileSerializer.is_valid():
                    uploadProfileSerializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse(pk, safe=False)
        # except:
        #     return JsonResponse("Invalid payload", safe=False)

