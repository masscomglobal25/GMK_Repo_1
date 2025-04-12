import os
from django.views.decorators.csrf import csrf_exempt
import requests
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from app_admin.models import CityRegion, EstimatedReach, Language, LocationType, MatchingCategory, NationalityCommunity, NearByAdvantage, VerticalType
from app_admin.serializers import CityRegionSerializer, EstimatedReachSerializer, LanguageSerializer, LocationTypeSerializer, MatchingCategorySerializer, NationalityCommunitySerializer, NearByAdvantageSerializer, VerticalTypeSerializer
from app_default.models import AdUnitCategory, UserType, Vertical, VerticalStatus
from app_default.serializers import AdUnitCategorySerializer, UserTypeSerializer, VerticalSerializer, VerticalStatusSerializer
from app_site.models import CampaignPDFData, Comments, Log, PriorityCode, SiteSettings
from django.db import connection

from app_site.serializers import CampaignPDFDataSerializer, CommentsSerializer, LogSerializer, PriorityCodeSerializer, SiteSettingsSerializer

# Create your views here.


@csrf_exempt
def CURDLogApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                log = Log.objects.all()
                logSerializer = LogSerializer(
                    log, many=True)
                # return JsonResponse(request.method, safe=False)
                return JsonResponse(logSerializer.data, safe=False)
            else:
                log = Log.objects.get(
                    LogId=pk)
                logSerializer = LogSerializer(
                    log)
                return JsonResponse(logSerializer.data, safe=False)
        elif request.method == 'POST':
            logData = JSONParser().parse(request)
            # return JsonResponse(logData, safe=False)
            logSerializer = LogSerializer(
                data=logData)
            if logSerializer.is_valid():
                logSerializer.save()
                return JsonResponse(logSerializer.data['LogId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            logData = JSONParser().parse(request)
            log = Log.objects.get(
                LogId=logData['LogId'])
            logSerializer = LogSerializer(
                log, data=logData)
            if logSerializer.is_valid():
                logSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDSiteSettingsApi(request, pk=""):
    try:
        if request.method == 'GET':
            siteSettings = SiteSettings.objects.all()
            siteSettingsSerializer = SiteSettingsSerializer(
                siteSettings, many=True)
            # return JsonResponse(request.method, safe=False)
            return JsonResponse(siteSettingsSerializer.data, safe=False)
        # elif request.method == 'POST':
        #     siteSettingsData = JSONParser().parse(request)
        #     # return JsonResponse(siteSettingsData, safe=False)
        #     siteSettingsSerializer = SiteSettingsSerializer(
        #         data=siteSettingsData)
        #     if siteSettingsSerializer.is_valid():
        #         siteSettingsSerializer.save()
        #         return JsonResponse(siteSettingsSerializer.data['SiteSettingId'], safe=False)
        #     return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            siteSettingsData = JSONParser().parse(request)
            siteSettings = SiteSettings.objects.get(
                SiteSettingId=siteSettingsData['SiteSettingId'])
            siteSettingsSerializer = SiteSettingsSerializer(
                siteSettings, data=siteSettingsData)
            if siteSettingsSerializer.is_valid():
                siteSettingsSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDCampaignPDFDataApi(request, UserId="", CampaignId=""):
    if request.method == 'POST':
        campaignPDFData = JSONParser().parse(request)
        campaignPDFDataSerializer = CampaignPDFDataSerializer(
            data=campaignPDFData)
        if campaignPDFDataSerializer.is_valid():
            campaignPDFDataSerializer.save()
            return JsonResponse('', safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'DELETE':
        campaignPDFData = CampaignPDFData.objects.filter(
            UserId=UserId, CampaignId=CampaignId)
        campaignPDFData.delete()
        return JsonResponse("Deleted successfully", safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)


@csrf_exempt
def SiteDetail(request):
    if request.method == 'GET':
        userType = UserType.objects.all()
        userTypeSerializer = UserTypeSerializer(userType, many=True)
        vertical = Vertical.objects.all()
        verticalSerializer = VerticalSerializer(vertical, many=True)
        # country = CountryEvent.objects.all()
        # countrySerializer = CountryEventSerializer(
        # country, many=True)
        cityRegion = CityRegion.objects.all()
        cityRegionSerializer = CityRegionSerializer(
            cityRegion, many=True)
        verticalStatus = VerticalStatus.objects.all()
        verticalStatusSerializer = VerticalStatusSerializer(
            verticalStatus, many=True)
        language = Language.objects.all()
        languageSerializer = LanguageSerializer(
            language, many=True)
        verticalType = VerticalType.objects.all()
        verticalTypeSerializer = VerticalTypeSerializer(
            verticalType, many=True)
        matchingCategory = MatchingCategory.objects.all()
        matchingCategorySerializer = MatchingCategorySerializer(
            matchingCategory, many=True)
        nationalityCommunity = NationalityCommunity.objects.all()
        nationalityCommunitySerializer = NationalityCommunitySerializer(
            nationalityCommunity, many=True)
        estimatedReach = EstimatedReach.objects.all()
        estimatedReachSerializer = EstimatedReachSerializer(
            estimatedReach, many=True)
        nearByAdvantages = NearByAdvantage.objects.all()
        nearByAdvantagesSerializer = NearByAdvantageSerializer(
            nearByAdvantages, many=True)
        locationType = LocationType.objects.all()
        locationTypeSerializer = LocationTypeSerializer(
            locationType, many=True)

        adUnitCategory = AdUnitCategory.objects.all()
        adUnitCategorySerializer = AdUnitCategorySerializer(
            adUnitCategory, many=True)
        # media = Media.objects.filter(
        #     ShowOnOff=1)
        # mediaSerializer = FilterMediaSerializer(
        #     media, many=True)
        siteSettings = SiteSettings.objects.all()
        siteSettingsSerializer = SiteSettingsSerializer(
            siteSettings, many=True)
        Data = []
        Data.append(userTypeSerializer.data)
        Data.append(verticalSerializer.data)
        Data.append(siteSettingsSerializer.data)
        Data.append(cityRegionSerializer.data)
        Data.append(verticalStatusSerializer.data)
        Data.append(languageSerializer.data)
        Data.append(verticalTypeSerializer.data)
        Data.append(matchingCategorySerializer.data)
        Data.append(nationalityCommunitySerializer.data)
        Data.append(estimatedReachSerializer.data)
        Data.append(nearByAdvantagesSerializer.data)
        Data.append(locationTypeSerializer.data)
        Data.append(adUnitCategorySerializer.data)
        return JsonResponse(Data, safe=False)

    else:
        return JsonResponse("Invalid request", safe=False)


@csrf_exempt
def CalenderHolidayAPI(request, CountryCode="", Year=""):
    try:
        if request.method == 'GET':
            r = requests.get('https://calendarific.com/api/v2/holidays?&api_key=f10a9b98fc7ae3a93b2587ef07b1e8b66e241171a6f96c9965dcf516d02592f4&country=' +
                             CountryCode+'&year='+Year+'', params=request.GET)
            if r.status_code == 200:
                return JsonResponse(r.json(), safe=False)
            return JsonResponse('Could not save data', safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def WebStatsAPI(request):
    try:
        if request.method == 'POST':
            Data = JSONParser().parse(request)
            url = "https://similar-web.p.rapidapi.com/get-analysis"

            querystring = {'domain': Data['WebURL']}

            headers = {
                'X-RapidAPI-Key': 'd108ff2349mshefca48c422c7423p1aa372jsn24c872be856e',
                'X-RapidAPI-Host': 'similar-web.p.rapidapi.com'
            }

            response = requests.get(url, headers=headers, params=querystring)

            if response.status_code == 200 and response.text != "SimilarWeb doesn't have enough data for this website.":
                return JsonResponse(response.text, safe=False)
            return JsonResponse("", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDCommentsApi(request, CommentType="", TypeId=""):
    try:
        if request.method == 'GET':
            comments = Comments.objects.filter(
                CommentType=CommentType, TypeId=TypeId)
            commentsSerializer = CommentsSerializer(
                comments, many=True)
            # return JsonResponse(request.method, safe=False)
            return JsonResponse(commentsSerializer.data, safe=False)
        elif request.method == 'POST':
            logData = JSONParser().parse(request)
            # return JsonResponse(logData, safe=False)
            commentsSerializer = CommentsSerializer(
                data=logData)
            if commentsSerializer.is_valid():
                commentsSerializer.save()
                return JsonResponse(commentsSerializer.data['CommentId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            logData = JSONParser().parse(request)
            comments = Comments.objects.get(
                CommentId=logData['CommentId'])
            commentsSerializer = CommentsSerializer(
                comments, data=logData)
            if commentsSerializer.is_valid():
                commentsSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def LinkedInAuth(request):
    try:
        client_id = "77koll3zob20n5"
        secret_id = "ukI0Dj8kUPJXPYqH"
        payload = {
            'form_params': {
                "grant_type": "authorization_code",
                "code": "AQQa8R1hZQciVs_LFMJdpR_mEEpkJSXA5MpO7cJZt_vvM3xSBNnudc6qQ8VvUsRaiuxuYINCHRTKrzC0--_lFydbzku6bZS9XeMJMJqgo7RNAnDu8maCIq3yULqxSftTFqEP4RdVuDnvsw9j0Ptss_MxQizh6sV6i2p5zaij_QmaKQA8GET3H79JQPibun9wUv2Zp9nHk7-6OCOAS5Q",
                "client_id": client_id,
                "client_secret": secret_id,
                "redirect_uri": "http://localhost:4200",
            }
        }
        r = requests.post(
            'https://www.linkedin.com/oauth/v2/accessToken', data=payload, params=request.POST)
        if r.status_code == 200:
            return JsonResponse(r.json(), safe=False)
        return JsonResponse(r.status_code, safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


# @csrf_exempt
# def renameFiles(request):
#     try:
#         i = 0
#         path="D:/python api/Server uploading/image/"
#         for filename in os.listdir(path):
#             my_dest =filename + ".webp"
#             my_source =path + filename
#             my_dest =path + my_dest
#             # rename() function will
#             # rename all the files
#             os.rename(my_source, my_dest)
#             i += 1
#         return JsonResponse("", safe=False)
#     except:
#         return JsonResponse("Invalid payload", safe=False)

@csrf_exempt
def CURDPriorityCodeApi(request, pk=""):
    # try:
    if request.method == 'GET':
        if not pk:
            priorityCode = PriorityCode.objects.all()
            priorityCodeSerializer = PriorityCodeSerializer(
                priorityCode, many=True)
            return JsonResponse(priorityCodeSerializer.data, safe=False)
        else:
            priorityCode = PriorityCode.objects.get(
                PriorityCodeId=pk)
            priorityCodeSerializer = PriorityCodeSerializer(
                priorityCode)
            return JsonResponse(priorityCodeSerializer.data, safe=False)
    elif request.method == 'POST':
        priorityCodeData = JSONParser().parse(request)
        # return JsonResponse(priorityCodeData, safe=False)
        priorityCodeSerializer = PriorityCodeSerializer(
            data=priorityCodeData)
        if priorityCodeSerializer.is_valid():
            priorityCodeSerializer.save()
            return JsonResponse(priorityCodeSerializer.data['PriorityCodeId'], safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        priorityCodeData = JSONParser().parse(request)
        priorityCode = PriorityCode.objects.get(
            PriorityCodeId=priorityCodeData['PriorityCodeId'])
        priorityCodeSerializer = PriorityCodeSerializer(
            priorityCode, data=priorityCodeData)
        if priorityCodeSerializer.is_valid():
            priorityCodeSerializer.save()
            return JsonResponse("Update successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        priorityCode = PriorityCode.objects.get(PriorityCodeId=pk)
        priorityCode.delete()
        return JsonResponse("Deleted successfully", safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDCheckPriorityCodeApi(request, Code=""):
    try:
        if request.method == 'GET':
            PlanCursor = connection.cursor()
            PlanCursor.execute("SELECT * FROM `app_site_prioritycode` WHERE BINARY `PriorityCode` = '" + Code + "'")

            PlanRow = PlanCursor.fetchall()
            return JsonResponse(PlanRow[0], safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("", safe=False)
