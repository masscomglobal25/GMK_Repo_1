from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from .models import OutOfHome, OutOfHomeMediaAdType, OutOfHomeMediaAdTypeImage
from .serializers import OutOfHomeMediaAdTypeSerializer, OutOfHomeSerializer, SaveOutOfHomeMediaAdTypeSerializer, SaveOutOfHomeSerializer, UploadOutOfHomeMediaAdTypeImageSerializer, UploadOutOfHomeMediaAdTypeSerializer, UploadOutOfHomeSerializer

# Create your views here.


@csrf_exempt
def CURDOutOfHomeApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                outOfHome = OutOfHome.objects.all()
                outOfHomeSerializer = OutOfHomeSerializer(
                    outOfHome, many=True)
                return JsonResponse(outOfHomeSerializer.data, safe=False)
            else:
                outOfHome = OutOfHome.objects.get(
                    OutOfHomeId=pk)
                outOfHomeSerializer = OutOfHomeSerializer(
                    outOfHome)
                return JsonResponse(outOfHomeSerializer.data, safe=False)
        elif request.method == 'POST':
            outOfHomeData = JSONParser().parse(request)

            outOfHomeSerializer = SaveOutOfHomeSerializer(
                data=outOfHomeData)
            if outOfHomeSerializer.is_valid():
                outOfHomeSerializer.save()
                return JsonResponse(outOfHomeSerializer.data['OutOfHomeId'], safe=False)
            return JsonResponse(outOfHomeSerializer.data, safe=False)
        elif request.method == 'PUT':
            outOfHomeData = JSONParser().parse(request)
            outOfHome = OutOfHome.objects.get(
                OutOfHomeId=outOfHomeData['OutOfHomeId'])
            outOfHomeSerializer = SaveOutOfHomeSerializer(
                outOfHome, data=outOfHomeData)
            if outOfHomeSerializer.is_valid():
                outOfHomeSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            outOfHome = OutOfHome.objects.get(OutOfHomeId=pk)
            outOfHome.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDPublisherOutOfHome(request, PublisherId=""):
    try:
        if request.method == 'GET':
            if PublisherId:
                outOfHome = OutOfHome.objects.filter(
                PublisherId=PublisherId)
                outOfHomeSerializer = OutOfHomeSerializer(
                    outOfHome, many=True)
                return JsonResponse(outOfHomeSerializer.data, safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


# def CURDOutOfHomeImageAPi(request, pk=""):
#     try:
#         if request.method == 'GET':
#             if not pk:
#                 outOfHomeImaage = OutOfHomeImage.objects.all()
#                 outOfHomeImaageSerializer = UploadOutOfHomeImageSerializer(
#                     outOfHomeImaage, many=True)
#                 return JsonResponse(outOfHomeImaageSerializer.data, safe=False)
#             else:
#                 outOfHomeImaage = OutOfHomeImage.objects.get(
#                     OutOfHomeId=pk)
#                 outOfHomeImaageSerializer = UploadOutOfHomeImageSerializer(
#                     outOfHomeImaage)
#                 return JsonResponse(outOfHomeImaageSerializer.data, safe=False)
#         else:
#             return JsonResponse("Invalid request", safe=False)
#     except:
#         return JsonResponse("Invalid payload", safe=False)


class OutOfHomeFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, pk="", ImageId="", *args, **kwargs):
        try:
            if not pk:
                file_serializer = UploadOutOfHomeSerializer(
                    data=request.data)
                if file_serializer.is_valid():
                    file_serializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse("failed", safe=False)
            else:
                outOfHome = OutOfHome.objects.get(
                    OutOfHomeId=pk)
                outOfHomeSerializer = UploadOutOfHomeSerializer(
                    outOfHome, data=request.data)
                if outOfHomeSerializer.is_valid():
                    outOfHomeSerializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse(pk, safe=False)
        except:
            return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDOutOfHomeMediaAdTypeApi(request, pk=""):
    # try:
    if request.method == 'GET':
        if not pk:
            outOfHomeMediaAdType = OutOfHomeMediaAdType.objects.all()
            outOfHomeMediaAdTypeSerializer = OutOfHomeMediaAdTypeSerializer(
                outOfHomeMediaAdType, many=True)
            return JsonResponse(outOfHomeMediaAdTypeSerializer.data, safe=False)
        else:

            outOfHomeMediaAdType = OutOfHomeMediaAdType.objects.get(
                OutOfHomeMediaAdTypeId=pk)
            outOfHomeMediaAdTypeSerializer = OutOfHomeMediaAdTypeSerializer(
                outOfHomeMediaAdType)
            return JsonResponse(outOfHomeMediaAdTypeSerializer.data, safe=False)
    elif request.method == 'POST':
        outOfHomeMediaAdTypeData = JSONParser().parse(request)

        outOfHomeMediaAdTypeSerializer = SaveOutOfHomeMediaAdTypeSerializer(
            data=outOfHomeMediaAdTypeData)
        if outOfHomeMediaAdTypeSerializer.is_valid():
            outOfHomeMediaAdTypeSerializer.save()
            return JsonResponse(outOfHomeMediaAdTypeSerializer.data['OutOfHomeMediaAdTypeId'], safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        outOfHomeMediaAdTypeData = JSONParser().parse(request)
        outOfHomeMediaAdType = OutOfHomeMediaAdType.objects.get(
            OutOfHomeMediaAdTypeId=outOfHomeMediaAdTypeData['OutOfHomeMediaAdTypeId'])
        outOfHomeMediaAdTypeSerializer = SaveOutOfHomeMediaAdTypeSerializer(
            outOfHomeMediaAdType, data=outOfHomeMediaAdTypeData)
        if outOfHomeMediaAdTypeSerializer.is_valid():
            outOfHomeMediaAdTypeSerializer.save()
            return JsonResponse("Update successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        outOfHomeMediaAdType = OutOfHomeMediaAdType.objects.get(
            OutOfHomeMediaAdTypeId=pk)
        outOfHomeMediaAdType.delete()
        return JsonResponse("Deleted successfully", safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


class OutOfHomeMediaAdTypeFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, pk="", *args, **kwargs):
        try:
            if not pk:
                file_serializer = UploadOutOfHomeMediaAdTypeSerializer(
                    data=request.data)
                if file_serializer.is_valid():
                    file_serializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse("failed", safe=False)
            else:
                outOfHomeMediaAdType = OutOfHomeMediaAdType.objects.get(
                    OutOfHomeMediaAdTypeId=pk)
                outOfHomeMediaAdTypeSerializer = UploadOutOfHomeMediaAdTypeSerializer(
                    outOfHomeMediaAdType, data=request.data)
                if outOfHomeMediaAdTypeSerializer.is_valid():
                    outOfHomeMediaAdTypeSerializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse(pk, safe=False)
        except:
            return JsonResponse("Invalid payload", safe=False)


class OutOfHomeMediaAdTypeImageFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, pk="", ImageId="", *args, **kwargs):
        try:
            if not ImageId:
                file_serializer = UploadOutOfHomeMediaAdTypeImageSerializer(
                    data=request.data)
                if file_serializer.is_valid():
                    file_serializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse("failed", safe=False)
            else:
                outOfHome = OutOfHome.objects.get(
                    OutOfHomeId=ImageId)
                outOfHomeSerializer = UploadOutOfHomeMediaAdTypeImageSerializer(
                    outOfHome, data=request.data)
                if outOfHomeSerializer.is_valid():
                    outOfHomeSerializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse(pk, safe=False)
        except:
            return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDOutOfHomeMediaAdTypeImageApi(request, outOfHomeId="", pk=""):
    try:
        if request.method == 'GET':
            # if not pk:
            outOfHomeMediaAdType = OutOfHomeMediaAdTypeImage.objects.all()
            outOfHomeMediaAdTypeSerializer = UploadOutOfHomeMediaAdTypeImageSerializer(
                outOfHomeMediaAdType, many=True)
            return JsonResponse(outOfHomeMediaAdTypeSerializer.data, safe=False)
            # else:
            #     outOfHomeMediaAdType = OutOfHomeMediaAdTypeImage.objects.filter(
            #         OutOfHomeMediaAdTypeId=pk, OutOfHomeId=outOfHomeId)
            #     outOfHomeMediaAdTypeSerializer = UploadOutOfHomeMediaAdTypeImageSerializer(
            #         outOfHomeMediaAdType)
            #     return JsonResponse(outOfHomeMediaAdTypeSerializer.data, safe=False)

        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)
