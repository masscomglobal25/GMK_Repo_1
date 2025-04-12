from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from app_ad_buzz.models import AdBuzz, AdBuzzImage
from app_ad_buzz.serializers import AdBuzzImageSerializer, AdBuzzSerializer
from app_admin.models import AdBuzzCategory
from app_admin.serializers import AdBuzzCategorySerializer


# Create your views here.

@csrf_exempt
def CURDAdBuzzApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                adBuzz = AdBuzz.objects.all()
                adBuzzSerializer = AdBuzzSerializer(
                    adBuzz, many=True)
                Data = []
                for adBuzz in adBuzzSerializer.data:
                    adBuzzDetail = []
                    adBuzzDetail.append(adBuzz)
                    adBuzzImage = AdBuzzImage.objects.filter(
                        AdBuzzId=adBuzz['AdBuzzId'])
                    adBuzzDetail.append(AdBuzzImageSerializer(
                        adBuzzImage, many=True).data)
                    Data.append(adBuzzDetail)
                return JsonResponse(Data, safe=False)
            else:
                adBuzz = AdBuzz.objects.get(
                    AdBuzzId=pk)
                adBuzzSerializer = AdBuzzSerializer(
                    adBuzz)
                Data = []
                Data.append(adBuzzSerializer.data)
                adBuzzImage = AdBuzzImage.objects.filter(
                    AdBuzzId=adBuzzSerializer.data['AdBuzzId'])
                Data.append(AdBuzzImageSerializer(
                    adBuzzImage, many=True).data)
                return JsonResponse(Data, safe=False)
        elif request.method == 'POST':
            adBuzzData = JSONParser().parse(request)
            adBuzzSerializer = AdBuzzSerializer(
                data=adBuzzData)
            if adBuzzSerializer.is_valid():
                adBuzzSerializer.save()
                return JsonResponse(adBuzzSerializer.data['AdBuzzId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            adBuzzData = JSONParser().parse(request)
            adBuzz = AdBuzz.objects.get(
                AdBuzzId=adBuzzData['AdBuzzId'])
            adBuzzSerializer = AdBuzzSerializer(
                adBuzz, data=adBuzzData)
            if adBuzzSerializer.is_valid():
                adBuzzSerializer.save()
                return JsonResponse(adBuzzSerializer.data['AdBuzzId'], safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            adBuzz = AdBuzz.objects.get(
                AdBuzzId=pk)
            # AdBuzzImage.objects.filter(
            #     AdBuzzId=pk).AdBuzzImageName.delete(save=True)
            AdBuzzImage.objects.filter(
                AdBuzzId=pk).delete()
            adBuzz.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)

@csrf_exempt
def GetAdBuzzByTagging(request, AdbuzzTagging=""):
    try:
        if request.method == 'GET':
            adBuzz = AdBuzz.objects.filter(
                AdbuzzTagging=AdbuzzTagging)
            adBuzzSerializer = AdBuzzSerializer(
                adBuzz, many=True)
            Data = []
            for adBuzz in adBuzzSerializer.data:
                adBuzzDetail = []
                adBuzzDetail.append(adBuzz)
                adBuzzImage = AdBuzzImage.objects.filter(
                    AdBuzzId=adBuzz['AdBuzzId'])
                adBuzzDetail.append(AdBuzzImageSerializer(
                    adBuzzImage, many=True).data)
                Data.append(adBuzzDetail)
            return JsonResponse(Data, safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


class UploadAdBuzzFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, pk="", *args, **kwargs):
        try:
            if not pk:
                file_serializer = AdBuzzImageSerializer(
                    data=request.data)
                if file_serializer.is_valid():
                    file_serializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse("failed", safe=False)
        except:
            return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDAdBuzzImageApi(request, pk=""):
    try:
        if request.method == 'DELETE':
            adBuzz = AdBuzzImage.objects.get(
                AdBuzzImageId=pk)
            AdBuzzImage.objects.get(
                AdBuzzImageId=pk).AdBuzzImageName.delete(save=True)
            adBuzz.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDAdBuzzTrendingApi(request, TrendingId=""):
    # try:
        if request.method == 'GET':
            adBuzzCategory = AdBuzzCategory.objects.get(
                AdBuzzCategory='Trending')
            adBuzzCategorySerializer = AdBuzzCategorySerializer(
                adBuzzCategory)
            adBuzz = AdBuzz.objects.filter(
                AdbuzzCategory=adBuzzCategorySerializer.data['AdBuzzCategoryId'])
            adBuzzSerializer = AdBuzzSerializer(
                adBuzz, many=True)
            Data = []
            for adBuzz in adBuzzSerializer.data:
                adBuzzDetail = []
                adBuzzDetail.append(adBuzz)
                adBuzzImage = AdBuzzImage.objects.filter(
                    AdBuzzId=adBuzz['AdBuzzId'])
                adBuzzDetail.append(AdBuzzImageSerializer(
                    adBuzzImage, many=True).data)
                Data.append(adBuzzDetail)
            return JsonResponse(Data, safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)
