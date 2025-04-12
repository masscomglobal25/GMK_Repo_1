from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from app_sales_marketing.models import SalesMarketing, SalesMarketingDetail
from app_sales_marketing.serializers import SalesMarketingDetailSerializer, SalesMarketingSerializer

# Create your views here.


@csrf_exempt
def CURDSalesMarketingApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                salesMarketing = SalesMarketing.objects.all()
                salesMarketingSerializer = SalesMarketingSerializer(
                    salesMarketing, many=True)
                return JsonResponse(salesMarketingSerializer.data, safe=False)
            else:
                salesMarketing = SalesMarketing.objects.get(
                    SalesMarketingId=pk)
                salesMarketingSerializer = SalesMarketingSerializer(
                    salesMarketing)
                return JsonResponse(salesMarketingSerializer.data, safe=False)
        elif request.method == 'POST':
            salesMarketingData = JSONParser().parse(request)
            # return JsonResponse(salesMarketingData, safe=False)
            salesMarketingSerializer = SalesMarketingSerializer(
                data=salesMarketingData)
            if salesMarketingSerializer.is_valid():
                salesMarketingSerializer.save()
                return JsonResponse(salesMarketingSerializer.data['SalesMarketingId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            salesMarketingData = JSONParser().parse(request)
            salesMarketing = SalesMarketing.objects.get(
                SalesMarketingId=salesMarketingData['SalesMarketingId'])
            salesMarketingSerializer = SalesMarketingSerializer(
                salesMarketing, data=salesMarketingData)
            if salesMarketingSerializer.is_valid():
                salesMarketingSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            salesMarketing = SalesMarketing.objects.get(
                SalesMarketingId=pk)
            salesMarketing.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDSalesMarketingDetailApi(request, SalesMarketingId="", pk=""):
    # try:
        if request.method == 'GET':
            if not pk:
                salesMarketingDetail = SalesMarketingDetail.objects.filter(
                    SalesMarketingId=SalesMarketingId)
                salesMarketingDetailSerializer = SalesMarketingDetailSerializer(
                    salesMarketingDetail, many=True)
                return JsonResponse(salesMarketingDetailSerializer.data, safe=False)
            else:
                salesMarketingDetail = SalesMarketingDetail.objects.get(
                    SalesMarketingDetailId=pk)
                salesMarketingDetailSerializer = SalesMarketingDetailSerializer(
                    salesMarketingDetail)
                return JsonResponse(salesMarketingDetailSerializer.data, safe=False)
        elif request.method == 'POST':
            salesMarketingDetailData = JSONParser().parse(request)
            # return JsonResponse(salesMarketingDetailData, safe=False)
            salesMarketingDetailSerializer = SalesMarketingDetailSerializer(
                data=salesMarketingDetailData)
            if salesMarketingDetailSerializer.is_valid():
                salesMarketingDetailSerializer.save()
                return JsonResponse(salesMarketingDetailSerializer.data['SalesMarketingDetailId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            salesMarketingDetailData = JSONParser().parse(request)
            salesMarketingDetail = SalesMarketingDetail.objects.get(
                SalesMarketingDetailId=salesMarketingDetailData['SalesMarketingDetailId'])
            salesMarketingDetailSerializer = SalesMarketingDetailSerializer(
                salesMarketingDetail, data=salesMarketingDetailData)
            if salesMarketingDetailSerializer.is_valid():
                salesMarketingDetailSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            salesMarketingDetail = SalesMarketingDetail.objects.get(
                SalesMarketingDetailId=pk)
            salesMarketingDetail.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)
