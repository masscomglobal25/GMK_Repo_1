from django.db import connection
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from app_page_seo.models import BoutiquePageSeo, PageSeo

from app_page_seo.serializers import BoutiquePageSeoSerializer, PageSeoSerializer

# Create your views here.


@csrf_exempt
def CURDPageSeoApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                pageSeo = PageSeo.objects.all()
                pageSeoSerializer = PageSeoSerializer(
                    pageSeo, many=True)
                return JsonResponse(pageSeoSerializer.data, safe=False)
            else:
                pageSeo = PageSeo.objects.get(
                    PageSeoId=pk)
                pageSeoSerializer = PageSeoSerializer(
                    pageSeo)
                return JsonResponse(pageSeoSerializer.data, safe=False)
        elif request.method == 'POST':
            pageSeoData = JSONParser().parse(request)
            # return JsonResponse(pageSeoData, safe=False)
            pageSeoSerializer = PageSeoSerializer(
                data=pageSeoData)
            if pageSeoSerializer.is_valid():
                pageSeoSerializer.save()
                return JsonResponse(pageSeoSerializer.data['PageSeoId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            pageSeoData = JSONParser().parse(request)
            pageSeo = PageSeo.objects.get(
                PageSeoId=pageSeoData['PageSeoId'])
            pageSeoSerializer = PageSeoSerializer(
                pageSeo, data=pageSeoData)
            if pageSeoSerializer.is_valid():
                pageSeoSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            pageSeo = PageSeo.objects.get(PageSeoId=pk)
            pageSeo.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDBoutiquePageSeoApi(request, CountryId="",AudienceId=""):
    try:
        if request.method == 'GET':
            if CountryId :
                boutiquePageSeo = BoutiquePageSeo.objects.get(
                    CountryId=CountryId,AudienceId=AudienceId)
                boutiquePageSeoSerializer = BoutiquePageSeoSerializer(
                    boutiquePageSeo)
                return JsonResponse(boutiquePageSeoSerializer.data, safe=False)
        elif request.method == 'POST':
            boutiquePageSeoData = JSONParser().parse(request)
            # return JsonResponse(boutiquePageSeoData, safe=False)
            boutiquePageSeoSerializer = BoutiquePageSeoSerializer(
                data=boutiquePageSeoData)
            if boutiquePageSeoSerializer.is_valid():
                boutiquePageSeoSerializer.save()
                return JsonResponse(boutiquePageSeoSerializer.data['BoutiquePageSeoId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            boutiquePageSeoData = JSONParser().parse(request)
            boutiquePageSeo = BoutiquePageSeo.objects.get(
                BoutiquePageSeoId=boutiquePageSeoData['BoutiquePageSeoId'])
            boutiquePageSeoSerializer = BoutiquePageSeoSerializer(
                boutiquePageSeo, data=boutiquePageSeoData)
            if boutiquePageSeoSerializer.is_valid():
                boutiquePageSeoSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            # boutiquePageSeo = BoutiquePageSeo.objects.get(BoutiquePageSeoId=pk)
            # boutiquePageSeo.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("", safe=False)
