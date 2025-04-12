from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from app_credit.models import AdvertiserCreditRequest, Credits
from app_credit.serializers import AdvertiserCreditRequestSerializer, CreditsSerializer
# Create your views here.


@csrf_exempt
def CreditsApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                credits = Credits.objects.all()
                creditsSerializer = CreditsSerializer(credits, many=True)
                return JsonResponse(creditsSerializer.data, safe=False)
            else:
                credits = Credits.objects.get(CreditId=pk)
                creditsSerializer = CreditsSerializer(credits)
                return JsonResponse(creditsSerializer.data, safe=False)

    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDCreditRequiredApi(request,  pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                advertiserCreditRequest = AdvertiserCreditRequest.objects.all()
                advertiserCreditRequestSerializer = AdvertiserCreditRequestSerializer(
                    advertiserCreditRequest, many=True)
                return JsonResponse(advertiserCreditRequestSerializer.data, safe=False)
            else:
                advertiserCreditRequest = AdvertiserCreditRequest.objects.get(
                    CreditRequiredId=pk)
                advertiserCreditRequestSerializer = AdvertiserCreditRequestSerializer(
                    advertiserCreditRequest)
                return JsonResponse(advertiserCreditRequestSerializer.data, safe=False)
        elif request.method == 'POST':
            cartData = JSONParser().parse(request)
            # return JsonResponse(cartData, safe=False)
            advertiserCreditRequestSerializer = AdvertiserCreditRequestSerializer(
                data=cartData)
            if advertiserCreditRequestSerializer.is_valid():
                advertiserCreditRequestSerializer.save()
                return JsonResponse(advertiserCreditRequestSerializer.data['CreditRequiredId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            cartData = JSONParser().parse(request)
            advertiserCreditRequest = AdvertiserCreditRequest.objects.get(
                CreditRequiredId=cartData['CreditRequiredId'])
            advertiserCreditRequestSerializer = AdvertiserCreditRequestSerializer(
                advertiserCreditRequest, data=cartData)
            if advertiserCreditRequestSerializer.is_valid():
                advertiserCreditRequestSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            advertiserCreditRequest = AdvertiserCreditRequest.objects.get(
                CreditRequiredId=pk)
            advertiserCreditRequest.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def HasCreditRequestAdvertiser(request,  UserId=""):
    # try:
        if request.method == 'GET':
            advertiserCreditRequest = AdvertiserCreditRequest.objects.filter(
                AdvertiserId=UserId)
            advertiserCreditRequestSerializer = AdvertiserCreditRequestSerializer(
                advertiserCreditRequest, many=True)
            # return JsonResponse(UserId, safe=False)
            return JsonResponse(advertiserCreditRequestSerializer.data, safe=False)
        else:
            return JsonResponse("", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)
