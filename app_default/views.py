from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import AdUnitCategorySerializer, AdvertiserAssistanceSupportSerializer, BotAavatarSerializer, CountryTypeSerializer, LightingTypeSerializer, OrganisationTypeSerializer, SaveVerticalSerializer, ServiceOrderUnitSerializer, ServiceUnitTypeSerializer, StaffPermissionSerializer, TimeZoneSerializer, UploadVerticalSerializer, UserTypeSerializer, VerticalSerializer, VerticalStatusSerializer

from .models import AdUnitCategory, AdvertiserAssistanceSupport, BotAavatar, CountryType, LightingType, OrganisationType, ServiceOrderUnit, ServiceUnitType, StaffPermission, TimeZone, UserType, Vertical, VerticalStatus

# Create your views here.


@csrf_exempt
def UserTypeApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                login = UserType.objects.all()
                login_serializer = UserTypeSerializer(login, many=True)
                return JsonResponse(login_serializer.data, safe=False)
            else:
                login = UserType.objects.get(LoginId=pk)
                login_serializer = UserTypeSerializer(login)
                return JsonResponse(login_serializer.data, safe=False)

    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def VerticalApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                vertical = Vertical.objects.all()
                verticalSerializer = VerticalSerializer(vertical, many=True)
                return JsonResponse(verticalSerializer.data, safe=False)
            else:
                vertical = Vertical.objects.get(VerticalId=pk)
                verticalSerializer = VerticalSerializer(vertical)
                return JsonResponse(verticalSerializer.data, safe=False)

    except:
        return JsonResponse("Invalid payload", safe=False)

@csrf_exempt
def CURDVerticalApi(request, pk=""):
    # try:
    if request.method == 'POST':
        verticalsData = JSONParser().parse(request)
        verticalsSerializer = SaveVerticalSerializer(
            data=verticalsData)
        # verticalsSerializer.is_valid()
        # return JsonResponse(verticalsSerializer.data, safe=False)
        if verticalsSerializer.is_valid():
            verticalsSerializer.save()
            return JsonResponse(verticalsSerializer.data['VerticalId'], safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        verticalsData = JSONParser().parse(request)
        verticals = Vertical.objects.get(
            VerticalId=verticalsData['VerticalId'])
        verticalsSerializer = SaveVerticalSerializer(
            verticals, data=verticalsData)
        if verticalsSerializer.is_valid():
            verticalsSerializer.save()
            return JsonResponse("Update successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


class VerticalFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, pk="", *args, **kwargs):
        try:
            if not pk:
                file_serializer = UploadVerticalSerializer(
                    data=request.data)
                if file_serializer.is_valid():
                    file_serializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse("failed", safe=False)
            else:
                verticals = Vertical.objects.get(
                    VerticalId=pk)
                # Vertical.objects.get(
                #     VerticalId=pk).VerticalIcon.delete(save=True)
                verticalsSerializer = UploadVerticalSerializer(
                    verticals, data=request.data)
                if verticalsSerializer.is_valid():
                    verticalsSerializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse(pk, safe=False)
        except:
            return JsonResponse("Invalid payload", safe=False)



@csrf_exempt
def CountryTypeApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                countryType = CountryType.objects.all()
                countryTypeSerializer = CountryTypeSerializer(countryType, many=True)
                return JsonResponse(countryTypeSerializer.data, safe=False)
            else:
                countryType = CountryType.objects.get(CountryTypeId=pk)
                countryTypeSerializer = CountryTypeSerializer(countryType)
                return JsonResponse(countryTypeSerializer.data, safe=False)

    except:
        return JsonResponse("Invalid payload", safe=False)

@csrf_exempt
def LightingTypeApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                lightingType = LightingType.objects.all()
                lightingTypeSerializer = LightingTypeSerializer(lightingType, many=True)
                return JsonResponse(lightingTypeSerializer.data, safe=False)
            else:
                lightingType = LightingType.objects.get(LightingTypeId=pk)
                lightingTypeSerializer = LightingTypeSerializer(lightingType)
                return JsonResponse(lightingTypeSerializer.data, safe=False)

    except:
        return JsonResponse("Invalid payload", safe=False)

@csrf_exempt
def VerticalStatusApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                verticalStatus = VerticalStatus.objects.all()
                verticalStatusSerializer = VerticalStatusSerializer(verticalStatus, many=True)
                return JsonResponse(verticalStatusSerializer.data, safe=False)
            else:
                verticalStatus = VerticalStatus.objects.get(VerticalStatusId=pk)
                verticalStatusSerializer = VerticalStatusSerializer(verticalStatus)
                return JsonResponse(verticalStatusSerializer.data, safe=False)

    except:
        return JsonResponse("Invalid payload", safe=False)

@csrf_exempt
def AdUnitCategoryApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                adUnitCategory = AdUnitCategory.objects.all()
                adUnitCategorySerializer = AdUnitCategorySerializer(adUnitCategory, many=True)
                return JsonResponse(adUnitCategorySerializer.data, safe=False)
            else:
                adUnitCategory = AdUnitCategory.objects.get(AdUnitCategoryId=pk)
                adUnitCategorySerializer = AdUnitCategorySerializer(adUnitCategory)
                return JsonResponse(adUnitCategorySerializer.data, safe=False)

    except:
        return JsonResponse("Invalid payload", safe=False)

@csrf_exempt
def TimeZoneApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                timeZone = TimeZone.objects.all()
                timeZoneSerializer = TimeZoneSerializer(timeZone, many=True)
                return JsonResponse(timeZoneSerializer.data, safe=False)
            else:
                timeZone = TimeZone.objects.get(TimeZoneId=pk)
                timeZoneSerializer = TimeZoneSerializer(timeZone)
                return JsonResponse(timeZoneSerializer.data, safe=False)

        elif request.method == 'POST':
            timeZoneData = JSONParser().parse(request)
            # return JsonResponse(timeZoneData, safe=False)
            timeZoneSerializer = TimeZoneSerializer(
                data=timeZoneData)
            if timeZoneSerializer.is_valid():
                timeZoneSerializer.save()
                return JsonResponse(timeZoneSerializer.data['TimeZoneId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            timeZoneData = JSONParser().parse(request)
            adBuzzCategory = TimeZone.objects.get(
                TimeZoneId=timeZoneData['TimeZoneId'])
            timeZoneSerializer = TimeZoneSerializer(
                adBuzzCategory, data=timeZoneData)
            if timeZoneSerializer.is_valid():
                timeZoneSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            adBuzzCategory = TimeZone.objects.get(
                TimeZoneId=pk)
            adBuzzCategory.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def ServiceUnitTypeApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                serviceUnitType = ServiceUnitType.objects.all()
                serviceUnitTypeSerializer = ServiceUnitTypeSerializer(serviceUnitType, many=True)
                return JsonResponse(serviceUnitTypeSerializer.data, safe=False)
            else:
                serviceUnitType = ServiceUnitType.objects.get(ServiceUnitTypeId=pk)
                serviceUnitTypeSerializer = ServiceUnitTypeSerializer(serviceUnitType)
                return JsonResponse(serviceUnitTypeSerializer.data, safe=False)

    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def ServiceOrderUnitApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                serviceOrderUnit = ServiceOrderUnit.objects.all()
                serviceOrderUnitSerializer = ServiceOrderUnitSerializer(serviceOrderUnit, many=True)
                return JsonResponse(serviceOrderUnitSerializer.data, safe=False)
            else:
                serviceOrderUnit = ServiceOrderUnit.objects.get(ServiceOrderUnitId=pk)
                serviceOrderUnitSerializer = ServiceOrderUnitSerializer(serviceOrderUnit)
                return JsonResponse(serviceOrderUnitSerializer.data, safe=False)

    except:
        return JsonResponse("Invalid payload", safe=False)

@csrf_exempt
def StaffPermissionApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                staffPermission = StaffPermission.objects.all()
                staffPermissionSerializer = StaffPermissionSerializer(staffPermission, many=True)
                return JsonResponse(staffPermissionSerializer.data, safe=False)
            else:
                staffPermission = StaffPermission.objects.get(StaffPermissionId=pk)
                staffPermissionSerializer = StaffPermissionSerializer(staffPermission)
                return JsonResponse(staffPermissionSerializer.data, safe=False)

    except:
        return JsonResponse("Invalid payload", safe=False)

@csrf_exempt
def AdvertiserAssistanceSupportApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                advertiserAssistanceSupport = AdvertiserAssistanceSupport.objects.all()
                advertiserAssistanceSupportSerializer = AdvertiserAssistanceSupportSerializer(advertiserAssistanceSupport, many=True)
                return JsonResponse(advertiserAssistanceSupportSerializer.data, safe=False)
            else:
                advertiserAssistanceSupport = AdvertiserAssistanceSupport.objects.get(AssistanceId=pk)
                advertiserAssistanceSupportSerializer = AdvertiserAssistanceSupportSerializer(advertiserAssistanceSupport)
                return JsonResponse(advertiserAssistanceSupportSerializer.data, safe=False)

    except:
        return JsonResponse("Invalid payload", safe=False)

@csrf_exempt
def OrganisationTypeApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                organisationType = OrganisationType.objects.all()
                organisationTypeSerializer = OrganisationTypeSerializer(organisationType, many=True)
                return JsonResponse(organisationTypeSerializer.data, safe=False)
            else:
                organisationType = OrganisationType.objects.get(OrganisationTypeId=pk)
                organisationTypeSerializer = OrganisationTypeSerializer(organisationType)
                return JsonResponse(organisationTypeSerializer.data, safe=False)

    except:
        return JsonResponse("Invalid payload", safe=False)

@csrf_exempt
def BotAavatarApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                botAavatar = BotAavatar.objects.all()
                botAavatarSerializer = BotAavatarSerializer(botAavatar, many=True)
                return JsonResponse(botAavatarSerializer.data, safe=False)
            else:
                botAavatar = BotAavatar.objects.get(BotAavatarId=pk)
                botAavatarSerializer = BotAavatarSerializer(botAavatar)
                return JsonResponse(botAavatarSerializer.data, safe=False)

    except:
        return JsonResponse("Invalid payload", safe=False)
