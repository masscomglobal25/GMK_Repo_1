from django.db import connection
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from .serializers import AdBuzzCategorySerializer, AdBuzzTaggingSerializer, AdFormatSerializer, AdUnitSpecificCategorySerializer, AdunitPositionSerializer, AdunitSizeSerializer, AgeGroupSerializer, BrandCategorySerializer, CampaignObjectiveSerializer, CampaignUnitSerializer, CityRegionSerializer, ContinentSerializer, CountryEventSerializer, EstimatedReachSerializer, GenderGroupSerializer, HelpRequiredForSerializer, HighlyRecommendedMediaSerializer, IncomeGroupSerializer, LanguageSerializer, LocationSerializer, LocationTypeSerializer, MatchingCategorySerializer, MediaCategorySerializer, NationalityCommunitySerializer, NearByAdvantageSerializer, RecommendationBannerSerializer, SaveAdUnitSpecificCategorySerializer, SaveAgeGroupSerializer, SaveCampaignUnitSerializer, SaveCountryEventSerializer, SaveGenderGroupSerializer, SaveIncomeGroupSerializer, SaveMatchingCategorySerializer, SaveMeetingRequestSerializer, SaveNearByAdvantageSerializer, SaveRecommendationBannerSerializer, SaveSiteBannerSerializer, SiteBannerSerializer, SiteMenuSerializer, UploadAdUnitSpecificCategorySerializer, UploadAgeGroupSerializer, UploadCampaignUnitSerializer, UploadCountryEventSerializer, UploadGenderGroupSerializer, UploadIncomeGroupSerializer, UploadMatchingCategorySerializer, UploadNearByAdvantageSerializer, UploadRecommendationBannerSerializer, UploadSiteBannerSerializer, VerticalTypeSerializer

from .models import AdBuzzCategory, AdBuzzTagging, AdFormat, AdUnitSpecificCategory, AdunitPosition, AdunitSize, AgeGroup, BrandCategory, CampaignObjective, CampaignUnit, CityRegion, Continent, CountryEvent, EstimatedReach, GenderGroup, HelpRequiredFor, HighlyRecommendedMedia, IncomeGroup, Language, Location, LocationType, MatchingCategory, MediaCategory, MeetingRequest, NationalityCommunity, NearByAdvantage, RecommendationBanner, SiteBanner, SiteMenu, VerticalType

from django.db.models import Max
# Create your views here.


@csrf_exempt
def CURDMatchingCategoryApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                matchingCategory = MatchingCategory.objects.all()
                matchingCategorySerializer = MatchingCategorySerializer(
                    matchingCategory, many=True)
                return JsonResponse(matchingCategorySerializer.data, safe=False)
            else:
                matchingCategory = MatchingCategory.objects.get(
                    MatchingCategoryId=pk)
                matchingCategorySerializer = MatchingCategorySerializer(
                    matchingCategory)
                return JsonResponse(matchingCategorySerializer.data, safe=False)
        elif request.method == 'POST':
            matchingCategoryData = JSONParser().parse(request)
            matchingCategorySerializer = SaveMatchingCategorySerializer(
                data=matchingCategoryData)
            if matchingCategorySerializer.is_valid():
                matchingCategorySerializer.save()
                category = matchingCategorySerializer.data
                last_id = MatchingCategory.objects.aggregate(
                    Max('Identification'))['Identification__max']
                category['Identification'] = last_id+1
                matchingCategory = MatchingCategory.objects.get(
                    MatchingCategoryId=matchingCategorySerializer.data['MatchingCategoryId'])
                Serializer2 = SaveCountryEventSerializer(
                    matchingCategory, category)
                if Serializer2.is_valid():
                    Serializer2.save()
                return JsonResponse(matchingCategorySerializer.data['MatchingCategoryId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            matchingCategoryData = JSONParser().parse(request)
            matchingCategory = MatchingCategory.objects.get(
                MatchingCategoryId=matchingCategoryData['MatchingCategoryId'])
            matchingCategorySerializer = SaveMatchingCategorySerializer(
                matchingCategory, data=matchingCategoryData)
            if matchingCategorySerializer.is_valid():
                matchingCategorySerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            matchingCategory = MatchingCategory.objects.get(
                MatchingCategoryId=pk)
            MatchingCategory.objects.get(
                MatchingCategoryId=pk).CategoryIcon.delete(save=True)
            matchingCategory.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


class MatchingCategoryFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, pk="", *args, **kwargs):
        try:
            if not pk:
                file_serializer = UploadMatchingCategorySerializer(
                    data=request.data)
                if file_serializer.is_valid():
                    file_serializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse("failed", safe=False)
            else:
                matchingCategory = MatchingCategory.objects.get(
                    MatchingCategoryId=pk)
                MatchingCategory.objects.get(
                    MatchingCategoryId=pk).CategoryIcon.delete(save=True)
                matchingCategorySerializer = UploadMatchingCategorySerializer(
                    matchingCategory, data=request.data)
                if matchingCategorySerializer.is_valid():
                    matchingCategorySerializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse(pk, safe=False)
        except:
            return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDNationalityCommunityApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                nationalityCommunity = NationalityCommunity.objects.all()
                nationalityCommunitySerializer = NationalityCommunitySerializer(
                    nationalityCommunity, many=True)
                return JsonResponse(nationalityCommunitySerializer.data, safe=False)
            else:
                nationalityCommunity = NationalityCommunity.objects.get(
                    NationalityCommunityId=pk)
                nationalityCommunitySerializer = NationalityCommunitySerializer(
                    nationalityCommunity)
                return JsonResponse(nationalityCommunitySerializer.data, safe=False)
        elif request.method == 'POST':
            nationalityCommunityData = JSONParser().parse(request)
            # return JsonResponse(nationalityCommunityData, safe=False)
            nationalityCommunitySerializer = NationalityCommunitySerializer(
                data=nationalityCommunityData)
            if nationalityCommunitySerializer.is_valid():
                nationalityCommunitySerializer.save()
                return JsonResponse(nationalityCommunitySerializer.data['NationalityCommunityId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            nationalityCommunityData = JSONParser().parse(request)
            nationalityCommunity = NationalityCommunity.objects.get(
                NationalityCommunityId=nationalityCommunityData['NationalityCommunityId'])
            nationalityCommunitySerializer = NationalityCommunitySerializer(
                nationalityCommunity, data=nationalityCommunityData)
            if nationalityCommunitySerializer.is_valid():
                nationalityCommunitySerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            nationalityCommunity = NationalityCommunity.objects.get(
                NationalityCommunityId=pk)
            nationalityCommunity.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDIncomeGroupApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                incomeGroup = IncomeGroup.objects.all()
                incomeGroupSerializer = IncomeGroupSerializer(
                    incomeGroup, many=True)
                return JsonResponse(incomeGroupSerializer.data, safe=False)
            else:
                incomeGroup = IncomeGroup.objects.get(
                    IncomeGroupId=pk)
                incomeGroupSerializer = IncomeGroupSerializer(
                    incomeGroup)
                return JsonResponse(incomeGroupSerializer.data, safe=False)
        elif request.method == 'POST':
            incomeGroupData = JSONParser().parse(request)
            incomeGroupSerializer = SaveIncomeGroupSerializer(
                data=incomeGroupData)
            if incomeGroupSerializer.is_valid():
                incomeGroupSerializer.save()
                return JsonResponse(incomeGroupSerializer.data['IncomeGroupId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            incomeGroupData = JSONParser().parse(request)
            incomeGroup = IncomeGroup.objects.get(
                IncomeGroupId=incomeGroupData['IncomeGroupId'])
            incomeGroupSerializer = SaveIncomeGroupSerializer(
                incomeGroup, data=incomeGroupData)
            if incomeGroupSerializer.is_valid():
                incomeGroupSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            incomeGroup = IncomeGroup.objects.get(IncomeGroupId=pk)
            IncomeGroup.objects.get(
                IncomeGroupId=pk).IncomeGroupIcon.delete(save=True)
            incomeGroup.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


class IncomeGroupFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, pk="", *args, **kwargs):
        try:
            if not pk:
                file_serializer = UploadIncomeGroupSerializer(
                    data=request.data)
                if file_serializer.is_valid():
                    file_serializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse("failed", safe=False)
            else:
                incomeGroup = IncomeGroup.objects.get(
                    IncomeGroupId=pk)
                IncomeGroup.objects.get(
                    IncomeGroupId=pk).IncomeGroupIcon.delete(save=True)
                incomeGroupSerializer = UploadIncomeGroupSerializer(
                    incomeGroup, data=request.data)
                if incomeGroupSerializer.is_valid():
                    incomeGroupSerializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse(pk, safe=False)
        except:
            return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDAgeGroupApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                ageGroup = AgeGroup.objects.all()
                ageGroupSerializer = AgeGroupSerializer(
                    ageGroup, many=True)
                return JsonResponse(ageGroupSerializer.data, safe=False)
            else:
                ageGroup = AgeGroup.objects.get(
                    AgeGroupId=pk)
                ageGroupSerializer = AgeGroupSerializer(
                    ageGroup)
                return JsonResponse(ageGroupSerializer.data, safe=False)
        elif request.method == 'POST':
            ageGroupData = JSONParser().parse(request)
            ageGroupSerializer = SaveAgeGroupSerializer(
                data=ageGroupData)
            if ageGroupSerializer.is_valid():
                ageGroupSerializer.save()
                return JsonResponse(ageGroupSerializer.data['AgeGroupId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            ageGroupData = JSONParser().parse(request)
            ageGroup = AgeGroup.objects.get(
                AgeGroupId=ageGroupData['AgeGroupId'])
            ageGroupSerializer = SaveAgeGroupSerializer(
                ageGroup, data=ageGroupData)
            if ageGroupSerializer.is_valid():
                ageGroupSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            ageGroup = AgeGroup.objects.get(AgeGroupId=pk)
            AgeGroup.objects.get(
                AgeGroupId=pk).AgeGroupIcon.delete(save=True)
            ageGroup.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


class AgeGroupFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, pk="", *args, **kwargs):
        try:
            if not pk:
                file_serializer = UploadAgeGroupSerializer(data=request.data)
                if file_serializer.is_valid():
                    file_serializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse("failed", safe=False)
            else:
                ageGroup = AgeGroup.objects.get(
                    AgeGroupId=pk)
                AgeGroup.objects.get(
                    AgeGroupId=pk).AgeGroupIcon.delete(save=True)
                ageGroupSerializer = UploadAgeGroupSerializer(
                    ageGroup, data=request.data)
                if ageGroupSerializer.is_valid():
                    ageGroupSerializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse(pk, safe=False)
        except:
            return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDGenderGroupApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                genderGroup = GenderGroup.objects.all()
                genderGroupSerializer = GenderGroupSerializer(
                    genderGroup, many=True)
                return JsonResponse(genderGroupSerializer.data, safe=False)
            else:
                genderGroup = GenderGroup.objects.get(
                    GenderGroupId=pk)
                genderGroupSerializer = GenderGroupSerializer(
                    genderGroup)
                return JsonResponse(genderGroupSerializer.data, safe=False)
        elif request.method == 'POST':
            genderGroupData = JSONParser().parse(request)
            genderGroupSerializer = SaveGenderGroupSerializer(
                data=genderGroupData)
            if genderGroupSerializer.is_valid():
                genderGroupSerializer.save()
                return JsonResponse(genderGroupSerializer.data['GenderGroupId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            genderGroupData = JSONParser().parse(request)
            genderGroup = GenderGroup.objects.get(
                GenderGroupId=genderGroupData['GenderGroupId'])
            genderGroupSerializer = SaveGenderGroupSerializer(
                genderGroup, data=genderGroupData)
            if genderGroupSerializer.is_valid():
                genderGroupSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            genderGroup = GenderGroup.objects.get(GenderGroupId=pk)
            GenderGroup.objects.get(
                GenderGroupId=pk).GenderGroupIcon.delete(save=True)
            genderGroup.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


class GenderGroupFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, pk="", *args, **kwargs):
        try:
            if not pk:
                file_serializer = UploadGenderGroupSerializer(
                    data=request.data)
                if file_serializer.is_valid():
                    file_serializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse("failed", safe=False)
            else:
                genderGroup = GenderGroup.objects.get(
                    GenderGroupId=pk)
                GenderGroup.objects.get(
                    GenderGroupId=pk).GenderGroupIcon.delete(save=True)
                genderGroupSerializer = UploadGenderGroupSerializer(
                    genderGroup, data=request.data)
                if genderGroupSerializer.is_valid():
                    genderGroupSerializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse(pk, safe=False)
        except:
            return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDLocationTypeApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                locationType = LocationType.objects.all()
                locationTypeSerializer = LocationTypeSerializer(
                    locationType, many=True)
                return JsonResponse(locationTypeSerializer.data, safe=False)
            else:
                locationType = LocationType.objects.get(
                    LocationTypeId=pk)
                locationTypeSerializer = LocationTypeSerializer(
                    locationType)
                return JsonResponse(locationTypeSerializer.data, safe=False)
        elif request.method == 'POST':
            locationTypeData = JSONParser().parse(request)
            # return JsonResponse(locationTypeData, safe=False)
            locationTypeSerializer = LocationTypeSerializer(
                data=locationTypeData)
            if locationTypeSerializer.is_valid():
                locationTypeSerializer.save()
                return JsonResponse(locationTypeSerializer.data['LocationTypeId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            locationTypeData = JSONParser().parse(request)
            locationType = LocationType.objects.get(
                LocationTypeId=locationTypeData['LocationTypeId'])
            locationTypeSerializer = LocationTypeSerializer(
                locationType, data=locationTypeData)
            if locationTypeSerializer.is_valid():
                locationTypeSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            locationType = LocationType.objects.get(LocationTypeId=pk)
            locationType.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDEstimatedReachApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                estimatedReach = EstimatedReach.objects.all()
                estimatedReachSerializer = EstimatedReachSerializer(
                    estimatedReach, many=True)
                return JsonResponse(estimatedReachSerializer.data, safe=False)
            else:
                estimatedReach = EstimatedReach.objects.get(
                    EstimatedReachId=pk)
                estimatedReachSerializer = EstimatedReachSerializer(
                    estimatedReach)
                return JsonResponse(estimatedReachSerializer.data, safe=False)
        elif request.method == 'POST':
            estimatedReachData = JSONParser().parse(request)
            # return JsonResponse(estimatedReachData, safe=False)
            estimatedReachSerializer = EstimatedReachSerializer(
                data=estimatedReachData)
            if estimatedReachSerializer.is_valid():
                estimatedReachSerializer.save()
                return JsonResponse(estimatedReachSerializer.data['EstimatedReachId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            estimatedReachData = JSONParser().parse(request)
            estimatedReach = EstimatedReach.objects.get(
                EstimatedReachId=estimatedReachData['EstimatedReachId'])
            estimatedReachSerializer = EstimatedReachSerializer(
                estimatedReach, data=estimatedReachData)
            if estimatedReachSerializer.is_valid():
                estimatedReachSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            estimatedReach = EstimatedReach.objects.get(EstimatedReachId=pk)
            estimatedReach.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDLanguageApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                language = Language.objects.all()
                languageSerializer = LanguageSerializer(
                    language, many=True)
                return JsonResponse(languageSerializer.data, safe=False)
            else:
                language = Language.objects.get(
                    LanguageId=pk)
                languageSerializer = LanguageSerializer(
                    language)
                return JsonResponse(languageSerializer.data, safe=False)
        elif request.method == 'POST':
            languageData = JSONParser().parse(request)
            # return JsonResponse(languageData, safe=False)
            languageSerializer = LanguageSerializer(
                data=languageData)
            if languageSerializer.is_valid():
                languageSerializer.save()
                return JsonResponse(languageSerializer.data['LanguageId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            languageData = JSONParser().parse(request)
            language = Language.objects.get(
                LanguageId=languageData['LanguageId'])
            languageSerializer = LanguageSerializer(
                language, data=languageData)
            if languageSerializer.is_valid():
                languageSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            language = Language.objects.get(LanguageId=pk)
            language.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDAdBuzzTaggingApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                adBuzzTagging = AdBuzzTagging.objects.all()
                adBuzzTaggingSerializer = AdBuzzTaggingSerializer(
                    adBuzzTagging, many=True)
                return JsonResponse(adBuzzTaggingSerializer.data, safe=False)
            else:
                adBuzzTagging = AdBuzzTagging.objects.get(
                    AdBuzzTaggingId=pk)
                adBuzzTaggingSerializer = AdBuzzTaggingSerializer(
                    adBuzzTagging)
                return JsonResponse(adBuzzTaggingSerializer.data, safe=False)
        elif request.method == 'POST':
            adBuzzTaggingData = JSONParser().parse(request)
            # return JsonResponse(adBuzzTaggingData, safe=False)
            adBuzzTaggingSerializer = AdBuzzTaggingSerializer(
                data=adBuzzTaggingData)
            if adBuzzTaggingSerializer.is_valid():
                adBuzzTaggingSerializer.save()
                return JsonResponse(adBuzzTaggingSerializer.data['AdBuzzTaggingId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            adBuzzTaggingData = JSONParser().parse(request)
            adBuzzTagging = AdBuzzTagging.objects.get(
                AdBuzzTaggingId=adBuzzTaggingData['AdBuzzTaggingId'])
            adBuzzTaggingSerializer = AdBuzzTaggingSerializer(
                adBuzzTagging, data=adBuzzTaggingData)
            if adBuzzTaggingSerializer.is_valid():
                adBuzzTaggingSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            adBuzzTagging = AdBuzzTagging.objects.get(AdBuzzTaggingId=pk)
            adBuzzTagging.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDVerticalTypeApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                verticalType = VerticalType.objects.all()
                verticalTypeSerializer = VerticalTypeSerializer(
                    verticalType, many=True)
                return JsonResponse(verticalTypeSerializer.data, safe=False)
            else:
                verticalType = VerticalType.objects.get(
                    VerticalTypeId=pk)
                verticalTypeSerializer = VerticalTypeSerializer(
                    verticalType)
                return JsonResponse(verticalTypeSerializer.data, safe=False)
        elif request.method == 'POST':
            verticalTypeData = JSONParser().parse(request)
            # return JsonResponse(verticalTypeData, safe=False)
            verticalTypeSerializer = VerticalTypeSerializer(
                data=verticalTypeData)
            if verticalTypeSerializer.is_valid():
                verticalTypeSerializer.save()
                return JsonResponse(verticalTypeSerializer.data['VerticalTypeId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            verticalTypeData = JSONParser().parse(request)
            verticalType = VerticalType.objects.get(
                VerticalTypeId=verticalTypeData['VerticalTypeId'])
            verticalTypeSerializer = VerticalTypeSerializer(
                verticalType, data=verticalTypeData)
            if verticalTypeSerializer.is_valid():
                verticalTypeSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            verticalType = VerticalType.objects.get(VerticalTypeId=pk)
            verticalType.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDContinentApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                continent = Continent.objects.all()
                continentSerializer = ContinentSerializer(
                    continent, many=True)
                return JsonResponse(continentSerializer.data, safe=False)
            else:
                continent = Continent.objects.get(
                    ContinentId=pk)
                continentSerializer = ContinentSerializer(
                    continent)
                return JsonResponse(continentSerializer.data, safe=False)
        elif request.method == 'POST':
            continentData = JSONParser().parse(request)
            # return JsonResponse(continentData, safe=False)
            continentSerializer = ContinentSerializer(
                data=continentData)
            if continentSerializer.is_valid():
                continentSerializer.save()
                return JsonResponse(continentSerializer.data['ContinentId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            continentData = JSONParser().parse(request)
            continent = Continent.objects.get(
                ContinentId=continentData['ContinentId'])
            continentSerializer = ContinentSerializer(
                continent, data=continentData)
            if continentSerializer.is_valid():
                continentSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            continent = Continent.objects.get(ContinentId=pk)
            continent.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDSEOCountryEventApi(request, pk=""):
    try:
        if request.method == 'GET':
            country = CountryEvent.objects.filter(
                OpenForSEO=1)
            countrySerializer = CountryEventSerializer(
                country, many=True)
            return JsonResponse(countrySerializer.data, safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDCountryEventApi(request, pk=""):
    # try:
    if request.method == 'GET':
        if not pk:
            country = CountryEvent.objects.all()
            countrySerializer = CountryEventSerializer(
                country, many=True)
            return JsonResponse(countrySerializer.data, safe=False)
        else:
            country = CountryEvent.objects.get(
                CountryEventId=pk)
            countrySerializer = CountryEventSerializer(
                country)
            return JsonResponse(countrySerializer.data, safe=False)
    elif request.method == 'POST':
        countryData = JSONParser().parse(request)
        countrySerializer = SaveCountryEventSerializer(
            data=countryData)
        # countrySerializer.is_valid()
        # return JsonResponse(countrySerializer.data, safe=False)
        if countrySerializer.is_valid():
            countrySerializer.save()
            country = countrySerializer.data
            last_id = CountryEvent.objects.aggregate(
                Max('Identification'))['Identification__max']
            country['Identification'] = last_id+1
            countryEvent = CountryEvent.objects.get(
                CountryEventId=countrySerializer.data['CountryEventId'])
            mediaSerializer2 = SaveCountryEventSerializer(
                countryEvent, country)
            if mediaSerializer2.is_valid():
                mediaSerializer2.save()
            return JsonResponse(countrySerializer.data['CountryEventId'], safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        countryData = JSONParser().parse(request)
        country = CountryEvent.objects.get(
            CountryEventId=countryData['CountryEventId'])
        countrySerializer = SaveCountryEventSerializer(
            country, data=countryData)
        if countrySerializer.is_valid():
            countrySerializer.save()
            return JsonResponse("Update successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        country = CountryEvent.objects.get(CountryEventId=pk)
        CountryEvent.objects.get(
            CountryEventId=pk).Logo.delete(save=True)
        CountryEvent.objects.get(
            CountryEventId=pk).InfoImage.delete(save=True)
        CountryEvent.objects.get(
            CountryEventId=pk).BannerImage.delete(save=True)
        country.delete()
        return JsonResponse("Deleted successfully", safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def DeleteCountryEventImage(request, FieldName="", pk=""):
    # try:
    if request.method == 'GET':
        if FieldName == 'Logo':
            CountryEvent.objects.get(
                CountryEventId=pk).Logo.delete(save=True)
        elif FieldName == 'InfoImage':
            CountryEvent.objects.get(
                CountryEventId=pk).InfoImage.delete(save=True)
        elif FieldName == 'BannerImage':
            CountryEvent.objects.get(
                CountryEventId=pk).BannerImage.delete(save=True)

        return JsonResponse("", safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDCountryEventHomePage(request, pk=""):
    # try:
    if request.method == 'GET':
        country = CountryEvent.objects.raw(
            "SELECT DISTINCT(`app_admin_countryevent`.`CountryEventId`) as CountryEventId ,`app_admin_countryevent`.`CountryEventName`,`app_admin_countryevent`.`AvailableVertical` FROM `app_admin_countryevent` JOIN `app_vertical_media_media` on `MediaId` IN (SELECT `MediaId` FROM `app_vertical_media_mediaadtype` WHERE `ShowOnOff`='1' AND (`Status`='2' OR Status='3')) and  `app_vertical_media_media`.`ShowOnOff`='1' AND ( `app_vertical_media_media`.`Status`='2' OR  `app_vertical_media_media`.Status='3') and  `app_vertical_media_media`.`CountryEvent` LIKE     CONCAT('%%',`app_admin_countryevent`.`CountryEventId` ,'%%')")
        countrySerializer = CountryEventSerializer(
            country, many=True)
        return JsonResponse(countrySerializer.data, safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


class CountryEventFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, pk="", *args, **kwargs):
        try:
            if not pk:
                file_serializer = UploadCountryEventSerializer(
                    data=request.data)
                if file_serializer.is_valid():
                    file_serializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse("failed", safe=False)
            else:
                country = CountryEvent.objects.get(
                    CountryEventId=pk)
                countrySerializer = UploadCountryEventSerializer(
                    country, data=request.data)
                if countrySerializer.is_valid():
                    countrySerializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse(pk, safe=False)
        except:
            return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CityRegionByCountry(request, pk=""):
    try:
        if request.method == 'GET':
    
            cityRegion = connection.cursor()
            cityRegion.execute("SELECT app_admin_cityregion.*,app_admin_countryevent.CountryEventName FROM `app_admin_cityregion` JOIN app_admin_countryevent ON app_admin_cityregion.CountryId=app_admin_countryevent.CountryEventId and app_admin_countryevent.CountryType='00520762-9b34-4124-bad6-d9f0a49d1dc8' ORDER BY app_admin_countryevent.CountryEventName ASC,app_admin_cityregion.CityRegionName ASC")
            field_names = [i[0] for i in cityRegion.description]
            media_mediaadtypeData = []
            for media in cityRegion.fetchall():
                j = 0
                MediaAdUnit = {}
                for col in media:
                    if j < len(field_names):
                        MediaAdUnit[str(field_names[j])] = col
                        j = j + 1
                media_mediaadtypeData.append(MediaAdUnit)
            if len(media_mediaadtypeData)>0:
                return JsonResponse(media_mediaadtypeData, safe=False)
            else:
                return JsonResponse("", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDCityRegionApi(request, pk=""):
    # try:
    if request.method == 'GET':
        if not pk:
            cityRegion = CityRegion.objects.all()
            cityRegionSerializer = CityRegionSerializer(
                cityRegion, many=True)
            return JsonResponse(cityRegionSerializer.data, safe=False)
        else:
            cityRegion = CityRegion.objects.get(
                CityId=pk)
            cityRegionSerializer = CityRegionSerializer(
                cityRegion)
            return JsonResponse(cityRegionSerializer.data, safe=False)
    elif request.method == 'POST':
        cityRegionData = JSONParser().parse(request)
        # return JsonResponse(cityRegionData, safe=False)
        cityRegionSerializer = CityRegionSerializer(
            data=cityRegionData)
        if cityRegionSerializer.is_valid():
            cityRegionSerializer.save()
            return JsonResponse(cityRegionSerializer.data['CityId'], safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        cityRegionData = JSONParser().parse(request)
        cityRegion = CityRegion.objects.get(
            CityId=cityRegionData['CityId'])
        cityRegionSerializer = CityRegionSerializer(
            cityRegion, data=cityRegionData)
        if cityRegionSerializer.is_valid():
            cityRegionSerializer.save()
            return JsonResponse("Update successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        cityRegion = CityRegion.objects.get(CityId=pk)
        cityRegion.delete()
        return JsonResponse("Deleted successfully", safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDLocationApi(request, pk=""):
    # try:
    if request.method == 'GET':
        if not pk:
            location = Location.objects.all()
            locationSerializer = LocationSerializer(
                location, many=True)
            return JsonResponse(locationSerializer.data, safe=False)
        else:
            location = Location.objects.get(
                LocationId=pk)
            locationSerializer = LocationSerializer(
                location)
            return JsonResponse(locationSerializer.data, safe=False)
    elif request.method == 'POST':
        locationData = JSONParser().parse(request)
        # return JsonResponse(locationData, safe=False)
        locationSerializer = LocationSerializer(
            data=locationData)
        if locationSerializer.is_valid():
            locationSerializer.save()
            return JsonResponse(locationSerializer.data['LocationId'], safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        locationData = JSONParser().parse(request)
        location = Location.objects.get(
            LocationId=locationData['LocationId'])
        locationSerializer = LocationSerializer(
            location, data=locationData)
        if locationSerializer.is_valid():
            locationSerializer.save()
            return JsonResponse("Update successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        location = Location.objects.get(LocationId=pk)
        location.delete()
        return JsonResponse("Deleted successfully", safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDNearByAdvantageApi(request, pk=""):
    # try:
    if request.method == 'GET':
        if not pk:
            nearByAdvantages = NearByAdvantage.objects.all()
            nearByAdvantagesSerializer = NearByAdvantageSerializer(
                nearByAdvantages, many=True)
            return JsonResponse(nearByAdvantagesSerializer.data, safe=False)
        else:
            nearByAdvantages = NearByAdvantage.objects.get(
                NearByAdvantageId=pk)
            nearByAdvantagesSerializer = NearByAdvantageSerializer(
                nearByAdvantages)
            return JsonResponse(nearByAdvantagesSerializer.data, safe=False)
    elif request.method == 'POST':
        nearByAdvantagesData = JSONParser().parse(request)
        nearByAdvantagesSerializer = SaveNearByAdvantageSerializer(
            data=nearByAdvantagesData)
        # nearByAdvantagesSerializer.is_valid()
        # return JsonResponse(nearByAdvantagesSerializer.data, safe=False)
        if nearByAdvantagesSerializer.is_valid():
            nearByAdvantagesSerializer.save()
            return JsonResponse(nearByAdvantagesSerializer.data['NearByAdvantageId'], safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        nearByAdvantagesData = JSONParser().parse(request)
        nearByAdvantages = NearByAdvantage.objects.get(
            NearByAdvantageId=nearByAdvantagesData['NearByAdvantageId'])
        nearByAdvantagesSerializer = SaveNearByAdvantageSerializer(
            nearByAdvantages, data=nearByAdvantagesData)
        if nearByAdvantagesSerializer.is_valid():
            nearByAdvantagesSerializer.save()
            return JsonResponse("Update successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        nearByAdvantages = NearByAdvantage.objects.get(NearByAdvantageId=pk)
        NearByAdvantage.objects.get(
            NearByAdvantageId=pk).NearByAdvantageIcon.delete(save=True)
        nearByAdvantages.delete()
        return JsonResponse("Deleted successfully", safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


class NearByAdvantageFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, pk="", *args, **kwargs):
        try:
            if not pk:
                file_serializer = UploadNearByAdvantageSerializer(
                    data=request.data)
                if file_serializer.is_valid():
                    file_serializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse("failed", safe=False)
            else:
                nearByAdvantages = NearByAdvantage.objects.get(
                    NearByAdvantageId=pk)
                NearByAdvantage.objects.get(
                    NearByAdvantageId=pk).NearByAdvantageIcon.delete(save=True)
                nearByAdvantagesSerializer = UploadNearByAdvantageSerializer(
                    nearByAdvantages, data=request.data)
                if nearByAdvantagesSerializer.is_valid():
                    nearByAdvantagesSerializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse(pk, safe=False)
        except:
            return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDAdunitPositionApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                adunitPosition = AdunitPosition.objects.all()
                adunitPositionSerializer = AdunitPositionSerializer(
                    adunitPosition, many=True)
                return JsonResponse(adunitPositionSerializer.data, safe=False)
            else:
                adunitPosition = AdunitPosition.objects.get(
                    AdunitPositionId=pk)
                adunitPositionSerializer = AdunitPositionSerializer(
                    adunitPosition)
                return JsonResponse(adunitPositionSerializer.data, safe=False)
        elif request.method == 'POST':
            adunitPositionData = JSONParser().parse(request)
            # return JsonResponse(adunitPositionData, safe=False)
            adunitPositionSerializer = AdunitPositionSerializer(
                data=adunitPositionData)
            if adunitPositionSerializer.is_valid():
                adunitPositionSerializer.save()
                return JsonResponse(adunitPositionSerializer.data['AdunitPositionId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            adunitPositionData = JSONParser().parse(request)
            adunitPosition = AdunitPosition.objects.get(
                AdunitPositionId=adunitPositionData['AdunitPositionId'])
            adunitPositionSerializer = AdunitPositionSerializer(
                adunitPosition, data=adunitPositionData)
            if adunitPositionSerializer.is_valid():
                adunitPositionSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            adunitPosition = AdunitPosition.objects.get(AdunitPositionId=pk)
            adunitPosition.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDAdunitSizeApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                adunitSize = AdunitSize.objects.all()
                adunitSizeSerializer = AdunitSizeSerializer(
                    adunitSize, many=True)
                return JsonResponse(adunitSizeSerializer.data, safe=False)
            else:
                adunitSize = AdunitSize.objects.get(
                    AdunitSizeId=pk)
                adunitSizeSerializer = AdunitSizeSerializer(
                    adunitSize)
                return JsonResponse(adunitSizeSerializer.data, safe=False)
        elif request.method == 'POST':
            adunitSizeData = JSONParser().parse(request)
            # return JsonResponse(adunitSizeData, safe=False)
            adunitSizeSerializer = AdunitSizeSerializer(
                data=adunitSizeData)
            if adunitSizeSerializer.is_valid():
                adunitSizeSerializer.save()
                return JsonResponse(adunitSizeSerializer.data['AdunitSizeId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            adunitSizeData = JSONParser().parse(request)
            adunitSize = AdunitSize.objects.get(
                AdunitSizeId=adunitSizeData['AdunitSizeId'])
            adunitSizeSerializer = AdunitSizeSerializer(
                adunitSize, data=adunitSizeData)
            if adunitSizeSerializer.is_valid():
                adunitSizeSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            adunitSize = AdunitSize.objects.get(AdunitSizeId=pk)
            adunitSize.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDMediaCategoryApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                mediaCategory = MediaCategory.objects.all()
                mediaCategorySerializer = MediaCategorySerializer(
                    mediaCategory, many=True)
                return JsonResponse(mediaCategorySerializer.data, safe=False)
            else:
                mediaCategory = MediaCategory.objects.get(
                    MediaCategoryId=pk)
                mediaCategorySerializer = MediaCategorySerializer(
                    mediaCategory)
                return JsonResponse(mediaCategorySerializer.data, safe=False)
        elif request.method == 'POST':
            mediaCategoryData = JSONParser().parse(request)
            # return JsonResponse(mediaCategoryData, safe=False)
            mediaCategorySerializer = MediaCategorySerializer(
                data=mediaCategoryData)
            if mediaCategorySerializer.is_valid():
                mediaCategorySerializer.save()
                return JsonResponse(mediaCategorySerializer.data['MediaCategoryId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            mediaCategoryData = JSONParser().parse(request)
            mediaCategory = MediaCategory.objects.get(
                MediaCategoryId=mediaCategoryData['MediaCategoryId'])
            mediaCategorySerializer = MediaCategorySerializer(
                mediaCategory, data=mediaCategoryData)
            if mediaCategorySerializer.is_valid():
                mediaCategorySerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            mediaCategory = MediaCategory.objects.get(MediaCategoryId=pk)
            mediaCategory.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDAdFormatApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                adFormat = AdFormat.objects.all()
                adFormatSerializer = AdFormatSerializer(
                    adFormat, many=True)
                return JsonResponse(adFormatSerializer.data, safe=False)
            else:
                adFormat = AdFormat.objects.get(
                    AdFormatId=pk)
                adFormatSerializer = AdFormatSerializer(
                    adFormat)
                return JsonResponse(adFormatSerializer.data, safe=False)
        elif request.method == 'POST':
            adFormatData = JSONParser().parse(request)
            # return JsonResponse(adFormatData, safe=False)
            adFormatSerializer = AdFormatSerializer(
                data=adFormatData)
            if adFormatSerializer.is_valid():
                adFormatSerializer.save()
                return JsonResponse(adFormatSerializer.data['AdFormatId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            adFormatData = JSONParser().parse(request)
            adFormat = AdFormat.objects.get(
                AdFormatId=adFormatData['AdFormatId'])
            adFormatSerializer = AdFormatSerializer(
                adFormat, data=adFormatData)
            if adFormatSerializer.is_valid():
                adFormatSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            adFormat = AdFormat.objects.get(AdFormatId=pk)
            adFormat.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDBrandCategoryApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                brandCategory = BrandCategory.objects.all()
                brandCategorySerializer = BrandCategorySerializer(
                    brandCategory, many=True)
                return JsonResponse(brandCategorySerializer.data, safe=False)
            else:
                brandCategory = BrandCategory.objects.get(
                    BrandCategoryId=pk)
                brandCategorySerializer = BrandCategorySerializer(
                    brandCategory)
                return JsonResponse(brandCategorySerializer.data, safe=False)
        elif request.method == 'POST':
            brandCategoryData = JSONParser().parse(request)
            # return JsonResponse(brandCategoryData, safe=False)
            brandCategorySerializer = BrandCategorySerializer(
                data=brandCategoryData)
            if brandCategorySerializer.is_valid():
                brandCategorySerializer.save()
                return JsonResponse(brandCategorySerializer.data['BrandCategoryId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            brandCategoryData = JSONParser().parse(request)
            brandCategory = BrandCategory.objects.get(
                BrandCategoryId=brandCategoryData['BrandCategoryId'])
            brandCategorySerializer = BrandCategorySerializer(
                brandCategory, data=brandCategoryData)
            if brandCategorySerializer.is_valid():
                brandCategorySerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            brandCategory = BrandCategory.objects.get(BrandCategoryId=pk)
            brandCategory.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDCampaignObjectiveApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                campaignObjective = CampaignObjective.objects.all()
                campaignObjectiveSerializer = CampaignObjectiveSerializer(
                    campaignObjective, many=True)
                return JsonResponse(campaignObjectiveSerializer.data, safe=False)
            else:
                campaignObjective = CampaignObjective.objects.get(
                    CampaignObjectiveId=pk)
                campaignObjectiveSerializer = CampaignObjectiveSerializer(
                    campaignObjective)
                return JsonResponse(campaignObjectiveSerializer.data, safe=False)
        elif request.method == 'POST':
            campaignObjectiveData = JSONParser().parse(request)
            # return JsonResponse(campaignObjectiveData, safe=False)
            campaignObjectiveSerializer = CampaignObjectiveSerializer(
                data=campaignObjectiveData)
            if campaignObjectiveSerializer.is_valid():
                campaignObjectiveSerializer.save()
                campaignObjective = campaignObjectiveSerializer.data
                last_id = CampaignObjective.objects.aggregate(
                    Max('Identification'))['Identification__max']
                campaignObjective['Identification'] = last_id+1
                campaignObjective2 = CampaignObjective.objects.get(
                    CampaignObjectiveId=campaignObjectiveSerializer.data['CampaignObjectiveId'])
                Serializer2 = CampaignObjectiveSerializer(
                    campaignObjective2, campaignObjective)
                if Serializer2.is_valid():
                    Serializer2.save()
                return JsonResponse(campaignObjectiveSerializer.data['CampaignObjectiveId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            campaignObjectiveData = JSONParser().parse(request)
            campaignObjective = CampaignObjective.objects.get(
                CampaignObjectiveId=campaignObjectiveData['CampaignObjectiveId'])
            campaignObjectiveSerializer = CampaignObjectiveSerializer(
                campaignObjective, data=campaignObjectiveData)
            if campaignObjectiveSerializer.is_valid():
                campaignObjectiveSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            campaignObjective = CampaignObjective.objects.get(
                CampaignObjectiveId=pk)
            campaignObjective.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDHelpRequiredForApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                campaignObjective = HelpRequiredFor.objects.all()
                campaignObjectiveSerializer = HelpRequiredForSerializer(
                    campaignObjective, many=True)
                return JsonResponse(campaignObjectiveSerializer.data, safe=False)
            else:
                campaignObjective = HelpRequiredFor.objects.get(
                    HelpRequiredForId=pk)
                campaignObjectiveSerializer = HelpRequiredForSerializer(
                    campaignObjective)
                return JsonResponse(campaignObjectiveSerializer.data, safe=False)
        elif request.method == 'POST':
            campaignObjectiveData = JSONParser().parse(request)
            # return JsonResponse(campaignObjectiveData, safe=False)
            campaignObjectiveSerializer = HelpRequiredForSerializer(
                data=campaignObjectiveData)
            if campaignObjectiveSerializer.is_valid():
                campaignObjectiveSerializer.save()
                return JsonResponse(campaignObjectiveSerializer.data['HelpRequiredForId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            campaignObjectiveData = JSONParser().parse(request)
            campaignObjective = HelpRequiredFor.objects.get(
                HelpRequiredForId=campaignObjectiveData['HelpRequiredForId'])
            campaignObjectiveSerializer = HelpRequiredForSerializer(
                campaignObjective, data=campaignObjectiveData)
            if campaignObjectiveSerializer.is_valid():
                campaignObjectiveSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            campaignObjective = HelpRequiredFor.objects.get(
                HelpRequiredForId=pk)
            campaignObjective.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDMeetingRequestApi(request, UserId="", UserType="", pk=""):
    # return JsonResponse(request.method, safe=False)
    try:
        if request.method == 'GET':
            if not pk and UserId:
                meetingRequest = MeetingRequest.objects.filter(
                    UserId=UserId, UserTypeId=UserType)
                saveMeetingRequestSerializer = SaveMeetingRequestSerializer(
                    meetingRequest, many=True)
                return JsonResponse(saveMeetingRequestSerializer.data, safe=False)
            elif pk:
                meetingRequest = MeetingRequest.objects.get(
                    MeetingRequestId=pk)
                saveMeetingRequestSerializer = SaveMeetingRequestSerializer(
                    meetingRequest)
                return JsonResponse(saveMeetingRequestSerializer.data, safe=False)
            else:
                meetingRequest = MeetingRequest.objects.all()
                saveMeetingRequestSerializer = SaveMeetingRequestSerializer(
                    meetingRequest, many=True)
                return JsonResponse(saveMeetingRequestSerializer.data, safe=False)

        elif request.method == 'POST':
            meetingRequestData = JSONParser().parse(request)
            saveMeetingRequestSerializer = SaveMeetingRequestSerializer(
                data=meetingRequestData)
            if saveMeetingRequestSerializer.is_valid():
                saveMeetingRequestSerializer.save()
                return JsonResponse(saveMeetingRequestSerializer.data['MeetingRequestId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            meetingRequestData = JSONParser().parse(request)
            meetingRequest = MeetingRequest.objects.get(
                MeetingRequestId=meetingRequestData['MeetingRequestId'])
            saveMeetingRequestSerializer = SaveMeetingRequestSerializer(
                meetingRequest, data=meetingRequestData)
            if saveMeetingRequestSerializer.is_valid():
                saveMeetingRequestSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            meetingRequest = MeetingRequest.objects.get(
                MeetingRequestId=pk)
            meetingRequest.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDMeetingRequestByUser(request, UserType=""):
    # return JsonResponse(request.method, safe=False)
    try:
        meetingRequest = MeetingRequest.objects.filter(
            UserTypeId=UserType)
        saveMeetingRequestSerializer = SaveMeetingRequestSerializer(
            meetingRequest, many=True)
        return JsonResponse(saveMeetingRequestSerializer.data, safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def IsUserRequestedForMeeting(request, UserId="", UserType="", pk=""):
    # return JsonResponse(request.method, safe=False)
    try:
        if request.method == 'POST':
            meetingRequestData = JSONParser().parse(request)
            meetingRequest = MeetingRequest.objects.filter(
                UserId=meetingRequestData['UserId'], HelpRequiredFor=meetingRequestData['MeetingType'])
            saveMeetingRequestSerializer = SaveMeetingRequestSerializer(
                meetingRequest, many=True)
            return JsonResponse(saveMeetingRequestSerializer.data, safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDAdUnitSpecificCategoryApi(request,  pk=""):
    # return JsonResponse(request.method, safe=False)
    # try:
    if request.method == 'GET':
        if pk:
            adUnitSpecificCategory = AdUnitSpecificCategory.objects.get(
                AdUnitSpecificCategoryId=pk)
            saveAdUnitSpecificCategorySerializer = AdUnitSpecificCategorySerializer(
                adUnitSpecificCategory)
            return JsonResponse(saveAdUnitSpecificCategorySerializer.data, safe=False)
        else:
            adUnitSpecificCategory = AdUnitSpecificCategory.objects.all()
            saveAdUnitSpecificCategorySerializer = AdUnitSpecificCategorySerializer(
                adUnitSpecificCategory, many=True)
            return JsonResponse(saveAdUnitSpecificCategorySerializer.data, safe=False)

    elif request.method == 'POST':
        adUnitSpecificCategoryData = JSONParser().parse(request)
        saveAdUnitSpecificCategorySerializer = SaveAdUnitSpecificCategorySerializer(
            data=adUnitSpecificCategoryData)
        if saveAdUnitSpecificCategorySerializer.is_valid():
            saveAdUnitSpecificCategorySerializer.save()
            AdUnitSpecific = saveAdUnitSpecificCategorySerializer.data
            last_id = AdUnitSpecificCategory.objects.aggregate(
                Max('Identification'))['Identification__max']
            AdUnitSpecific['Identification'] = last_id+1
            adUnitSpecificCategory = AdUnitSpecificCategory.objects.get(
                AdUnitSpecificCategoryId=saveAdUnitSpecificCategorySerializer.data['AdUnitSpecificCategoryId'])
            Serializer2 = AdUnitSpecificCategorySerializer(
                adUnitSpecificCategory, AdUnitSpecific)
            if Serializer2.is_valid():
                Serializer2.save()
            return JsonResponse(saveAdUnitSpecificCategorySerializer.data['AdUnitSpecificCategoryId'], safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        adUnitSpecificCategoryData = JSONParser().parse(request)
        adUnitSpecificCategory = AdUnitSpecificCategory.objects.get(
            AdUnitSpecificCategoryId=adUnitSpecificCategoryData['AdUnitSpecificCategoryId'])
        saveAdUnitSpecificCategorySerializer = SaveAdUnitSpecificCategorySerializer(
            adUnitSpecificCategory, data=adUnitSpecificCategoryData)
        if saveAdUnitSpecificCategorySerializer.is_valid():
            saveAdUnitSpecificCategorySerializer.save()
            return JsonResponse("Update successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        adUnitSpecificCategory = AdUnitSpecificCategory.objects.get(
            AdUnitSpecificCategoryId=pk)
        adUnitSpecificCategory.delete()
        return JsonResponse("Deleted successfully", safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


class AdUnitSpecificCategoryFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, pk="", *args, **kwargs):
        try:
            if not pk:
                file_serializer = UploadAdUnitSpecificCategorySerializer(
                    data=request.data)
                if file_serializer.is_valid():
                    file_serializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse("failed", safe=False)
            else:
                adUnitSpecificCategorys = AdUnitSpecificCategory.objects.get(
                    AdUnitSpecificCategoryId=pk)
                AdUnitSpecificCategory.objects.get(
                    AdUnitSpecificCategoryId=pk).AdUnitSpecificCategoryIcon.delete(save=True)
                adUnitSpecificCategorysSerializer = UploadAdUnitSpecificCategorySerializer(
                    adUnitSpecificCategorys, data=request.data)
                if adUnitSpecificCategorysSerializer.is_valid():
                    adUnitSpecificCategorysSerializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse(pk, safe=False)
        except:
            return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDHighlyRecommendedMediaApi(request,  pk=""):
    # return JsonResponse(request.method, safe=False)
    # try:
    if request.method == 'GET':
        if pk:
            highlyRecommendedMedia = HighlyRecommendedMedia.objects.get(
                HighlyRecommendedMediaId=pk)
            saveHighlyRecommendedMediaSerializer = HighlyRecommendedMediaSerializer(
                highlyRecommendedMedia)
            return JsonResponse(saveHighlyRecommendedMediaSerializer.data, safe=False)
        else:
            highlyRecommendedMedia = HighlyRecommendedMedia.objects.all()
            saveHighlyRecommendedMediaSerializer = HighlyRecommendedMediaSerializer(
                highlyRecommendedMedia, many=True)
            return JsonResponse(saveHighlyRecommendedMediaSerializer.data, safe=False)

    elif request.method == 'POST':
        highlyRecommendedMediaData = JSONParser().parse(request)
        saveHighlyRecommendedMediaSerializer = HighlyRecommendedMediaSerializer(
            data=highlyRecommendedMediaData)
        if saveHighlyRecommendedMediaSerializer.is_valid():
            saveHighlyRecommendedMediaSerializer.save()
            return JsonResponse(saveHighlyRecommendedMediaSerializer.data['HighlyRecommendedMediaId'], safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        highlyRecommendedMediaData = JSONParser().parse(request)
        highlyRecommendedMedia = HighlyRecommendedMedia.objects.get(
            HighlyRecommendedMediaId=highlyRecommendedMediaData['HighlyRecommendedMediaId'])
        saveHighlyRecommendedMediaSerializer = HighlyRecommendedMediaSerializer(
            highlyRecommendedMedia, data=highlyRecommendedMediaData)
        if saveHighlyRecommendedMediaSerializer.is_valid():
            saveHighlyRecommendedMediaSerializer.save()
            return JsonResponse("Update successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        highlyRecommendedMedia = HighlyRecommendedMedia.objects.get(
            HighlyRecommendedMediaId=pk)
        highlyRecommendedMedia.delete()
        return JsonResponse("Deleted successfully", safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDHighlyRecommendedMediaByAudienceId(request, CountryId,  AudienceId=""):
    # return JsonResponse(request.method, safe=False)
    # try:
    if request.method == 'GET':
        highlyRecommendedMedia = HighlyRecommendedMedia.objects.filter(
            AudienceId=AudienceId, CountryId=CountryId)
        saveHighlyRecommendedMediaSerializer = HighlyRecommendedMediaSerializer(
            highlyRecommendedMedia, many=True)
        return JsonResponse(saveHighlyRecommendedMediaSerializer.data, safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDRecommendationBannerApi(request,  pk=""):
    # return JsonResponse(request.method, safe=False)
    # try:
    if request.method == 'GET':
        if pk:
            recommendationBannerMedia = RecommendationBanner.objects.get(
                RecommendationBannerId=pk)
            saveRecommendationBannerSerializer = RecommendationBannerSerializer(
                recommendationBannerMedia)
            return JsonResponse(saveRecommendationBannerSerializer.data, safe=False)
        else:
            recommendationBannerMedia = RecommendationBanner.objects.all()
            saveRecommendationBannerSerializer = RecommendationBannerSerializer(
                recommendationBannerMedia, many=True)
            return JsonResponse(saveRecommendationBannerSerializer.data, safe=False)

    elif request.method == 'POST':
        recommendationBannerMediaData = JSONParser().parse(request)
        saveRecommendationBannerSerializer = SaveRecommendationBannerSerializer(
            data=recommendationBannerMediaData)
        if saveRecommendationBannerSerializer.is_valid():
            saveRecommendationBannerSerializer.save()
            return JsonResponse(saveRecommendationBannerSerializer.data['RecommendationBannerId'], safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        recommendationBannerMediaData = JSONParser().parse(request)
        recommendationBannerMedia = RecommendationBanner.objects.get(
            RecommendationBannerId=recommendationBannerMediaData['RecommendationBannerId'])
        saveRecommendationBannerSerializer = SaveRecommendationBannerSerializer(
            recommendationBannerMedia, data=recommendationBannerMediaData)
        if saveRecommendationBannerSerializer.is_valid():
            saveRecommendationBannerSerializer.save()
            return JsonResponse("Update successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        recommendationBanners = RecommendationBanner.objects.get(
            RecommendationBannerId=pk)
        RecommendationBanner.objects.get(
            RecommendationBannerId=pk).BannerImage.delete(save=True)
        RecommendationBanner.objects.get(
            RecommendationBannerId=pk).BannerImageForMobile.delete(save=True)
        recommendationBannerMedia = RecommendationBanner.objects.get(
            RecommendationBannerId=pk)
        recommendationBannerMedia.delete()
        return JsonResponse("Deleted successfully", safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDRecommendationBannerByAudienceId(request, CountryId,  AudienceId=""):
    # return JsonResponse(request.method, safe=False)
    # try:
    if request.method == 'GET':
        mediaAdType = connection.cursor()
        mediaAdType.execute(
            "SELECT recommendationbanner.*, media.MediaAdType,media.Identification as AdUnitIdentification, media.SiteName, media.MediaAdUnitDescription, media.PackageName, media.AdTypeEstimateReached, media.MediaId, media.MediaIdentification , media.MediaName , media.VerticalType FROM (SELECT * FROM `app_admin_recommendationbanner` WHERE app_admin_recommendationbanner.AudienceId='"+AudienceId+"' AND  app_admin_recommendationbanner.CountryId='"+CountryId+"') AS recommendationbanner LEFT JOIN (SELECT app_vertical_media_mediaadtype.*,app_vertical_media_media.Identification as MediaIdentification,app_vertical_media_media.MediaName,app_vertical_media_media.VerticalType FROM `app_vertical_media_mediaadtype` JOIN app_vertical_media_media on app_vertical_media_mediaadtype.MediaId = app_vertical_media_media.MediaId) as media ON recommendationbanner.AdUnit=media.MediaAdTypeId")
        field_names = [i[0] for i in mediaAdType.description]
        allMediaAdUnit = []
        for media in mediaAdType.fetchall():
            j = 0
            MediaAdUnit = {}
            for col in media:
                if j < len(field_names):
                    MediaAdUnit[str(field_names[j])] = col
                    j = j + 1
            allMediaAdUnit.append(MediaAdUnit)

        return JsonResponse(allMediaAdUnit, safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


class RecommendationBannerFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, pk="", *args, **kwargs):
        # try:
        if not pk:
            file_serializer = UploadRecommendationBannerSerializer(
                data=request.data)
            if file_serializer.is_valid():
                file_serializer.save()
                return JsonResponse("ok", safe=False)
            else:
                return JsonResponse("failed", safe=False)
        else:
            recommendationBanners = RecommendationBanner.objects.get(
                RecommendationBannerId=pk)
            # RecommendationBanner.objects.get(
            #     RecommendationBannerId=pk).BannerImage.delete(save=True)
            recommendationBannersSerializer = UploadRecommendationBannerSerializer(
                recommendationBanners, data=request.data)
            if recommendationBannersSerializer.is_valid():
                recommendationBannersSerializer.save()
                return JsonResponse("ok", safe=False)
            else:
                return JsonResponse(pk, safe=False)
        # except:
        #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDSiteBannerApi(request,  pk=""):
    # return JsonResponse(request.method, safe=False)
    # try:
    if request.method == 'GET':
        if pk:
            siteBannerMedia = SiteBanner.objects.get(
                SiteBannerId=pk)
            saveSiteBannerSerializer = SiteBannerSerializer(
                siteBannerMedia)
            return JsonResponse(saveSiteBannerSerializer.data, safe=False)
        else:
            siteBannerMedia = SiteBanner.objects.all()
            saveSiteBannerSerializer = SiteBannerSerializer(
                siteBannerMedia, many=True)
            return JsonResponse(saveSiteBannerSerializer.data, safe=False)

    elif request.method == 'POST':
        siteBannerMediaData = JSONParser().parse(request)
        saveSiteBannerSerializer = SaveSiteBannerSerializer(
            data=siteBannerMediaData)
        if saveSiteBannerSerializer.is_valid():
            saveSiteBannerSerializer.save()
            return JsonResponse(saveSiteBannerSerializer.data['SiteBannerId'], safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        siteBannerMediaData = JSONParser().parse(request)
        siteBannerMedia = SiteBanner.objects.get(
            SiteBannerId=siteBannerMediaData['SiteBannerId'])
        saveSiteBannerSerializer = SaveSiteBannerSerializer(
            siteBannerMedia, data=siteBannerMediaData)
        if saveSiteBannerSerializer.is_valid():
            saveSiteBannerSerializer.save()
            return JsonResponse("Update successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        siteBanners = SiteBanner.objects.get(
            SiteBannerId=pk)
        SiteBanner.objects.get(
            SiteBannerId=pk).BannerImage.delete(save=True)
        SiteBanner.objects.get(
            SiteBannerId=pk).BannerImageForMobile.delete(save=True)
        siteBannerMedia = SiteBanner.objects.get(
            SiteBannerId=pk)
        siteBannerMedia.delete()
        return JsonResponse("Deleted successfully", safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDSiteBanner(request, CountryId,  AudienceId="",  CategoryId=""):
    # return JsonResponse(request.method, safe=False)
    # try:
    if request.method == 'GET':
        mediaAdType = connection.cursor()
        mediaAdType.execute(
            "SELECT sitebanner.*, media.MediaAdType,media.Identification as AdUnitIdentification, media.SiteName, media.MediaAdUnitDescription, media.PackageName, media.AdTypeEstimateReached, media.MediaId, media.MediaIdentification , media.MediaName , media.VerticalType FROM (SELECT * FROM `app_admin_sitebanner` WHERE app_admin_sitebanner.AudienceId='"+AudienceId+"' AND  app_admin_sitebanner.CountryId='"+CountryId+"' AND  app_admin_sitebanner.CategoryId='"+CategoryId+"') AS sitebanner LEFT JOIN (SELECT app_vertical_media_mediaadtype.*,app_vertical_media_media.Identification as MediaIdentification,app_vertical_media_media.MediaName,app_vertical_media_media.VerticalType FROM `app_vertical_media_mediaadtype` JOIN app_vertical_media_media on app_vertical_media_mediaadtype.MediaId = app_vertical_media_media.MediaId) as media ON sitebanner.AdUnit=media.MediaAdTypeId")
        field_names = [i[0] for i in mediaAdType.description]
        allMediaAdUnit = []
        for media in mediaAdType.fetchall():
            j = 0
            MediaAdUnit = {}
            for col in media:
                if j < len(field_names):
                    MediaAdUnit[str(field_names[j])] = col
                    j = j + 1
            allMediaAdUnit.append(MediaAdUnit)

        return JsonResponse(allMediaAdUnit, safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)

@csrf_exempt
def getSiteBannerMulti(request):
    # return JsonResponse(request.method, safe=False)
    # try:
    if request.method == 'POST':
        BannerFilterData = JSONParser().parse(request)
        
        CountryId=""
        for x in BannerFilterData['Country']:
            if CountryId:
                CountryId = CountryId+","
            CountryId = CountryId+" '"+ x +"' "
        AudienceId=""
        for x in BannerFilterData['Audience']:
            if AudienceId:
                AudienceId = AudienceId+","
            AudienceId = AudienceId+" '"+ x +"' "
        CategoryId=""
        for x in BannerFilterData['Category']:
            if CategoryId:
                CategoryId = CategoryId+","
            CategoryId = CategoryId+" '"+ x +"' "
        
        mediaAdType = connection.cursor()
        mediaAdType.execute(
            "SELECT sitebanner.*, media.MediaAdType,media.Identification as AdUnitIdentification, media.SiteName, media.MediaAdUnitDescription, media.PackageName, media.AdTypeEstimateReached, media.MediaId, media.MediaIdentification , media.MediaName , media.VerticalType FROM (SELECT * FROM `app_admin_sitebanner` WHERE app_admin_sitebanner.AudienceId IN ("+AudienceId+") AND  app_admin_sitebanner.CountryId IN ("+CountryId+") AND  app_admin_sitebanner.CategoryId IN ("+CategoryId+")) AS sitebanner LEFT JOIN (SELECT app_vertical_media_mediaadtype.*,app_vertical_media_media.Identification as MediaIdentification,app_vertical_media_media.MediaName,app_vertical_media_media.VerticalType FROM `app_vertical_media_mediaadtype` JOIN app_vertical_media_media on app_vertical_media_mediaadtype.MediaId = app_vertical_media_media.MediaId) as media ON sitebanner.AdUnit=media.MediaAdTypeId")
        field_names = [i[0] for i in mediaAdType.description]
        allMediaAdUnit = []
        for media in mediaAdType.fetchall():
            j = 0
            MediaAdUnit = {}
            for col in media:
                if j < len(field_names):
                    MediaAdUnit[str(field_names[j])] = col
                    j = j + 1
            allMediaAdUnit.append(MediaAdUnit)

        return JsonResponse(allMediaAdUnit, safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


class SiteBannerFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, pk="", *args, **kwargs):
        # try:
        if not pk:
            file_serializer = UploadSiteBannerSerializer(
                data=request.data)
            if file_serializer.is_valid():
                file_serializer.save()
                return JsonResponse("ok", safe=False)
            else:
                return JsonResponse("failed", safe=False)
        else:
            siteBanners = SiteBanner.objects.get(
                SiteBannerId=pk)
            # SiteBanner.objects.get(
            #     SiteBannerId=pk).BannerImage.delete(save=True)
            siteBannersSerializer = UploadSiteBannerSerializer(
                siteBanners, data=request.data)
            if siteBannersSerializer.is_valid():
                siteBannersSerializer.save()
                return JsonResponse("ok", safe=False)
            else:
                return JsonResponse(pk, safe=False)
        # except:
        #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDAdBuzzCategoryApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                adBuzzCategory = AdBuzzCategory.objects.all()
                adBuzzCategorySerializer = AdBuzzCategorySerializer(
                    adBuzzCategory, many=True)
                return JsonResponse(adBuzzCategorySerializer.data, safe=False)
            else:
                adBuzzCategory = AdBuzzCategory.objects.get(
                    AdBuzzCategoryId=pk)
                adBuzzCategorySerializer = AdBuzzCategorySerializer(
                    adBuzzCategory)
                return JsonResponse(adBuzzCategorySerializer.data, safe=False)
        elif request.method == 'POST':
            adBuzzCategoryData = JSONParser().parse(request)
            # return JsonResponse(adBuzzCategoryData, safe=False)
            adBuzzCategorySerializer = AdBuzzCategorySerializer(
                data=adBuzzCategoryData)
            if adBuzzCategorySerializer.is_valid():
                adBuzzCategorySerializer.save()
                return JsonResponse(adBuzzCategorySerializer.data['AdBuzzCategoryId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            adBuzzCategoryData = JSONParser().parse(request)
            adBuzzCategory = AdBuzzCategory.objects.get(
                AdBuzzCategoryId=adBuzzCategoryData['AdBuzzCategoryId'])
            adBuzzCategorySerializer = AdBuzzCategorySerializer(
                adBuzzCategory, data=adBuzzCategoryData)
            if adBuzzCategorySerializer.is_valid():
                adBuzzCategorySerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            adBuzzCategory = AdBuzzCategory.objects.get(
                AdBuzzCategoryId=pk)
            adBuzzCategory.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDCampaignUnitApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                campaignUnit = CampaignUnit.objects.all()
                campaignUnitSerializer = CampaignUnitSerializer(
                    campaignUnit, many=True)
                return JsonResponse(campaignUnitSerializer.data, safe=False)
            else:
                campaignUnit = CampaignUnit.objects.get(
                    CampaignUnitId=pk)
                campaignUnitSerializer = CampaignUnitSerializer(
                    campaignUnit)
                return JsonResponse(campaignUnitSerializer.data, safe=False)
        elif request.method == 'POST':
            campaignUnitData = JSONParser().parse(request)
            campaignUnitSerializer = SaveCampaignUnitSerializer(
                data=campaignUnitData)
            if campaignUnitSerializer.is_valid():
                campaignUnitSerializer.save()
                return JsonResponse(campaignUnitSerializer.data['CampaignUnitId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            campaignUnitData = JSONParser().parse(request)
            campaignUnit = CampaignUnit.objects.get(
                CampaignUnitId=campaignUnitData['CampaignUnitId'])
            campaignUnitSerializer = SaveCampaignUnitSerializer(
                campaignUnit, data=campaignUnitData)
            if campaignUnitSerializer.is_valid():
                campaignUnitSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            campaignUnit = CampaignUnit.objects.get(
                CampaignUnitId=pk)
            CampaignUnit.objects.get(
                CampaignUnitId=pk).CampaignUnitIcon.delete(save=True)
            campaignUnit.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


class CampaignUnitFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, pk="", *args, **kwargs):
        try:
            if not pk:
                file_serializer = UploadCampaignUnitSerializer(
                    data=request.data)
                if file_serializer.is_valid():
                    file_serializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse("failed", safe=False)
            else:
                campaignUnit = CampaignUnit.objects.get(
                    CampaignUnitId=pk)
                CampaignUnit.objects.get(
                    CampaignUnitId=pk).CampaignUnitIcon.delete(save=True)
                campaignUnitSerializer = UploadCampaignUnitSerializer(
                    campaignUnit, data=request.data)
                if campaignUnitSerializer.is_valid():
                    campaignUnitSerializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse(pk, safe=False)
        except:
            return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDSiteMenuApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                siteMenu = SiteMenu.objects.all()
                siteMenuSerializer = SiteMenuSerializer(
                    siteMenu, many=True)
                return JsonResponse(siteMenuSerializer.data, safe=False)
            else:
                siteMenu = SiteMenu.objects.get(
                    SiteMenuId=pk)
                siteMenuSerializer = SiteMenuSerializer(
                    siteMenu)
                return JsonResponse(siteMenuSerializer.data, safe=False)
        elif request.method == 'POST':
            siteMenuData = JSONParser().parse(request)
            siteMenuSerializer = SiteMenuSerializer(
                data=siteMenuData)
            if siteMenuSerializer.is_valid():
                siteMenuSerializer.save()
                return JsonResponse(siteMenuSerializer.data['SiteMenuId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            siteMenuData = JSONParser().parse(request)
            siteMenu = SiteMenu.objects.get(
                SiteMenuId=siteMenuData['SiteMenuId'])
            siteMenuSerializer = SiteMenuSerializer(
                siteMenu, data=siteMenuData)
            if siteMenuSerializer.is_valid():
                siteMenuSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            siteMenu = SiteMenu.objects.get(
                SiteMenuId=pk)
            siteMenu.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)
