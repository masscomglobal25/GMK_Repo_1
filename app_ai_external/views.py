from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import json
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from app_admin.models import CityRegion, CountryEvent, Language, MatchingCategory, MediaCategory
from app_admin.serializers import CityRegionSerializer, CountryEventSerializer, LanguageSerializer, MatchingCategorySerializer, MediaCategorySerializer
from app_ai_external.models import AIFilteredData
from app_ai_external.serializers import AIFilteredDataSerializer
from app_default.models import AdUnitCategory, MediaAdType
from app_default.serializers import AdUnitCategorySerializer
from app_vertical_media.models import Media,MediaAdTypeWithMediaView
from app_vertical_media.serializers import MediaAdTypeSerializer, MediaSerializer

# Create your views here.


@csrf_exempt
def GetTagCountries(request, pk=""):
    try:
        if request.method == 'GET':
            sql = "SELECT `CountryEvent` FROM `app_vertical_media_media` WHERE Status IN ('2','3') AND ShowOnOff='1' and MediaId in (SELECT `MediaId` FROM `app_vertical_media_mediaadtype` WHERE Status IN ('2','3') AND ShowOnOff='1')"
            cursor = connection.cursor()
            cursor.execute(sql)
            data_id = {}
            data_id = "''"
            for data in cursor.fetchall():
                id = json.loads(data[0])
                for media_ROW in id:
                    data_id = data_id+",'"+media_ROW+"'"
            sql = "SELECT `CountryEventId`,`CountryEventName` FROM `app_admin_countryevent` WHERE `CountryOnOFF`='1' and CountryEventId IN (" + \
                data_id+") "
            countryevent = connection.cursor()
            countryevent.execute(sql)
            field_names = [i[0] for i in countryevent.description]
            countryeventData = []
            for media in countryevent.fetchall():
                j = 0
                MediaAdUnit = {}
                for col in media:
                    if j < len(field_names):
                        MediaAdUnit[str(field_names[j])] = col
                        j = j + 1
                countryeventData.append(MediaAdUnit)

        return JsonResponse(countryeventData, safe=False)
    except:
        p = ""

@csrf_exempt
def CountryEventApi(request, pk=""):
    try:
        if request.method == 'GET':
            sql = "SELECT `CountryEventId`, `CountryEventName`,app_default_countrytype.CountryType,Description FROM `app_admin_countryevent` JOIN app_default_countrytype on app_admin_countryevent.CountryType=app_default_countrytype.CountryTypeId and `CountryOnOFF`='1'"
            countryevent = connection.cursor()
            countryevent.execute(sql)
            field_names = [i[0] for i in countryevent.description]
            countryeventData = []
            for media in countryevent.fetchall():
                j = 0
                MediaAdUnit = {}
                for col in media:
                    if j < len(field_names):
                        MediaAdUnit[str(field_names[j])] = col
                        j = j + 1
                countryeventData.append(MediaAdUnit)

        return JsonResponse(countryeventData, safe=False)
    except:
        p = ""


@csrf_exempt
def CityRegionApi(request, pk=""):
    try:
        if request.method == 'GET':
            sql = "SELECT `CityId`,`CityRegionName`,app_admin_countryevent.CountryEventName FROM `app_admin_cityregion` JOIN app_admin_countryevent on app_admin_cityregion.CountryId=app_admin_countryevent.CountryEventId;"
            countryevent = connection.cursor()
            countryevent.execute(sql)
            field_names = [i[0] for i in countryevent.description]
            countryeventData = []
            for media in countryevent.fetchall():
                j = 0
                MediaAdUnit = {}
                for col in media:
                    if j < len(field_names):
                        MediaAdUnit[str(field_names[j])] = col
                        j = j + 1
                countryeventData.append(MediaAdUnit)

        return JsonResponse(countryeventData, safe=False)
    except:
        p = ""



@csrf_exempt
def GetTagDetailsByCountry(request, CountryEventId=""):
    try:
        if request.method == 'GET':
            sql = "SELECT `PrimaryLanguage`,`MediaId`,`CityRegion`,`Language` FROM `app_vertical_media_media` WHERE  Status IN ('2','3') AND ShowOnOff='1' and MediaId in (SELECT `MediaId` FROM `app_vertical_media_mediaadtype` WHERE Status IN ('2','3') AND ShowOnOff='1') and `CountryEvent` LIKE '%%" + \
                CountryEventId+"%%'  "

            vertical_media = connection.cursor()
            vertical_media.execute(sql)
            field_names = [i[0] for i in vertical_media.description]
            vertical_mediaData = []
            for media in vertical_media.fetchall():
                j = 0
                MediaAdUnit = {}
                for col in media:
                    if j < len(field_names):
                        MediaAdUnit[str(field_names[j])] = col
                        j = j + 1
                vertical_mediaData.append(MediaAdUnit)
            CityRegion_id = "''"
            Language_id = "''"
            MediaId_id = "''"
            for media in vertical_mediaData:
                try:
                    id = json.loads(media['CityRegion'])
                    for media_ROW in id:
                        CityRegion_id = CityRegion_id+",'"+media_ROW+"'"
                except:
                    p = ""
                # id = json.loads(media['MediaId'])
                # for media_ROW in id:
                MediaId_id = MediaId_id+",'"+media['MediaId']+"'"
                try:
                    id = json.loads(media['Language'])
                    Language_id = Language_id+",'"+media['PrimaryLanguage']+"'"
                    for media_ROW in id:
                        Language_id = Language_id+",'"+media_ROW+"'"
                except:
                    p = ""

            # return JsonResponse(Language_id, safe=False)
            sql = "SELECT `MatchingCategories`,`AgeGroup`,`GenderGroup`,`IncomeGroup` FROM `app_vertical_media_mediaadtype` WHERE   Status IN ('2','3') AND ShowOnOff='1' and `MediaId` in ("+MediaId_id+")"
            media_mediaadtype = connection.cursor()
            media_mediaadtype.execute(sql)
            field_names = [i[0] for i in media_mediaadtype.description]
            media_mediaadtypeData = []
            for media in media_mediaadtype.fetchall():
                j = 0
                MediaAdUnit = {}
                for col in media:
                    if j < len(field_names):
                        MediaAdUnit[str(field_names[j])] = col
                        j = j + 1
                media_mediaadtypeData.append(MediaAdUnit)
            MatchingCategories_id = "''"
            for media in media_mediaadtypeData:
                try:
                    id = json.loads(media['MatchingCategories'])
                    for media_ROW in id:
                        MatchingCategories_id = MatchingCategories_id+",'"+media_ROW+"'"
                except:
                    p = ""
                # id = json.loads(media['MediaId'])
                # for media_ROW in id:
                #     MediaId_id = MediaId_id+",'"+media_ROW+"'"
                # id = json.loads(media['Language'])
                # Language_id = Language_id+",'"+media['PrimaryLanguage']+"'"
                # for media_ROW in id:
                #     Language_id = Language_id+",'"+media_ROW+"'"
            result_data = []
            sql = "SELECT `CityId`,`CityRegionName`,`CountryId` FROM `app_admin_cityregion` WHERE `CityId` in (" + \
                CityRegion_id+")"
            cityregion = connection.cursor()
            cityregion.execute(sql)
            field_names = [i[0] for i in cityregion.description]
            cityregionData = []
            for media in cityregion.fetchall():
                j = 0
                MediaAdUnit = {}
                for col in media:
                    if j < len(field_names):
                        MediaAdUnit[str(field_names[j])] = col
                        j = j + 1
                cityregionData.append(MediaAdUnit)
            sql = "SELECT `LanguageId`,`Language` FROM `app_admin_language` WHERE `LanguageId` in (" + \
                Language_id+")"
            language = connection.cursor()
            language.execute(sql)
            field_names = [i[0] for i in language.description]
            languageData = []
            for media in language.fetchall():
                j = 0
                MediaAdUnit = {}
                for col in media:
                    if j < len(field_names):
                        MediaAdUnit[str(field_names[j])] = col
                        j = j + 1
                languageData.append(MediaAdUnit)
            sql = "SELECT `MatchingCategoryId`,`MatchingCategory` FROM `app_admin_matchingcategory` WHERE `MatchingCategoryId` in (" + \
                MatchingCategories_id+")"
            matchingcategory = connection.cursor()
            matchingcategory.execute(sql)
            field_names = [i[0] for i in matchingcategory.description]
            matchingcategoryData = []
            for media in matchingcategory.fetchall():
                j = 0
                MediaAdUnit = {}
                for col in media:
                    if j < len(field_names):
                        MediaAdUnit[str(field_names[j])] = col
                        j = j + 1
                matchingcategoryData.append(MediaAdUnit)
            # result_data['MatchingCategory']=matchingcategoryData
            # result_data['Language']=languageData
            # result_data['City']=cityregionData
            result_data = {
                'MatchingCategory': matchingcategoryData,
                'Language': languageData,
                'City': cityregionData,
            }
            return JsonResponse(result_data, safe=False)
    except:
        p = ""


@csrf_exempt
def MediaFromAIApi(request, UserId=""):

    aIFilteredData = AIFilteredData.objects.get(
        UserId=UserId)
    aIFilteredDataSerializer = AIFilteredDataSerializer(
        aIFilteredData).data
    WhereClause = ""
    if aIFilteredDataSerializer['Country']:
        WhereClause = WhereClause + \
            " JSON_CONTAINS(m.CountryEventJSON, '"+'"' + \
            aIFilteredDataSerializer['Country']+'"'+"') "
    if aIFilteredDataSerializer['CityRegion']:
        if WhereClause:
            WhereClause = WhereClause + " AND "
        WhereClause = WhereClause + \
            " JSON_CONTAINS(m.CityRegionJSON, '"+'"' + \
            aIFilteredDataSerializer['CityRegion']+'"'+"') "
    if aIFilteredDataSerializer['MediaType']:
        if WhereClause:
            WhereClause = WhereClause + " AND "
        WhereClause = WhereClause + " VerticalType = '" + \
            aIFilteredDataSerializer['MediaType']+"'"
    # if aIFilteredDataSerializer['CampaignType']:
    #     if WhereClause:
    #         WhereClause = WhereClause +  " AND "
    #     WhereClause = WhereClause + " JSON_CONTAINS(m.CountryEventJSON, '"+'"'+aIFilteredDataSerializer['Country']+'"'+"') "
    if aIFilteredDataSerializer['Language']:
        if WhereClause:
            WhereClause = WhereClause + " AND "
        WhereClause = WhereClause + \
            " JSON_CONTAINS(m.LanguageJSON, '"+'"' + \
            aIFilteredDataSerializer['Language']+'"'+"') "
    if WhereClause:
        WhereClause = " WHERE "+WhereClause
    sql = "SELECT * FROM app_vertical_media_mediaadtype AS ad JOIN app_vertical_media_media AS m ON ad.MediaId = m.MediaId " + WhereClause

    media_mediaadtype = connection.cursor()
    media_mediaadtype.execute(sql)
    field_names = [i[0] for i in media_mediaadtype.description]
    media_mediaadtypeData = []
    for media in media_mediaadtype.fetchall():
        j = 0
        MediaAdUnit = {}
        for col in media:
            if j < len(field_names):
                MediaAdUnit[str(field_names[j])] = col
                j = j + 1
        media_mediaadtypeData.append(MediaAdUnit)
    if len(media_mediaadtypeData) > 0:
        return JsonResponse(media_mediaadtypeData, safe=False)
    else:
        return JsonResponse("", safe=False)


@csrf_exempt
def CURDAIFilteredDataApi(request, UserId=""):
    # try:
    if request.method == 'GET':
        if not UserId:
            aIFilteredData = AIFilteredData.objects.all()
            aIFilteredDataSerializer = AIFilteredDataSerializer(
                aIFilteredData, many=True)
            return JsonResponse(aIFilteredDataSerializer.data, safe=False)
        else:
            aIFilteredData = AIFilteredData.objects.filter(
                UserId=UserId).order_by('-SortId')
            aIFilteredDataSerializer = AIFilteredDataSerializer(
                aIFilteredData,many=True)
            data=aIFilteredDataSerializer.data[0]
            AdUnitId=""
            for media in data['AIJsonData']:
                if AdUnitId:
                    AdUnitId = AdUnitId+","
                try:
                    AdUnitId = AdUnitId+"'"+media['AdUnitId']+"'"
                except:
                    try:
                        AdUnitId = AdUnitId+"'"+media['AdunitId']+"'"
                    except:
                        p=""
            if AdUnitId=="":
                AdUnitId="'NoAdUnitId'"
            # return JsonResponse("SELECT * FROM `app_vertical_media_media` WHERE ViewOnlyMediaStore='0' AND Status IN ('2','3') AND ShowOnOff='1' AND MediaId IN (SELECT MediaId FROM `app_vertical_media_mediaadtype` WHERE `MediaAdTypeId` IN (" + AdUnitId + ")) ", safe=False)
            
            media = Media.objects.raw(
                "SELECT * FROM `app_vertical_media_media` WHERE ViewOnlyMediaStore='0' AND Status IN ('2','3') AND ShowOnOff='1' AND MediaId IN (SELECT MediaId FROM `app_vertical_media_mediaadtype` WHERE `MediaAdTypeId` IN (" + AdUnitId + ")) ")

            mediaSerializer = MediaSerializer(
                media, many=True)

            mediaAdType = MediaAdType.objects.raw(
                "SELECT * FROM `app_vertical_media_mediaadtype` WHERE `MediaAdTypeId` IN (" + AdUnitId + ")")

            mediaAdTypeSerializer = MediaAdTypeSerializer(
                mediaAdType, many=True)
            data['MediaDetails']=[]
            data['MediaDetails'].append(mediaSerializer.data)
            data['MediaDetails'].append(mediaAdTypeSerializer.data)
            # media_mediaadtype = connection.cursor()
            # media_mediaadtype.execute(
            #     aIFilteredDataSerializer.data['SQLQuery'])
            # field_names = [i[0] for i in media_mediaadtype.description]
            # media_mediaadtypeData = []
            # for media in media_mediaadtype.fetchall():
            #     j = 0
            #     MediaAdUnit = {}
            #     for col in media:
            #         if j < len(field_names):
            #             MediaAdUnit[str(field_names[j])] = col
            #             j = j + 1
            #     media_mediaadtypeData.append(MediaAdUnit)
            return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        aIFilteredDataData = JSONParser().parse(request)
        try:
            aIFilteredData = AIFilteredData.objects.all(
                UserId=aIFilteredDataData['UserId'])
            aIFilteredData.delete()
        except:
            p = 1
        aIFilteredDataSerializer = AIFilteredDataSerializer(
            data=aIFilteredDataData)
        if aIFilteredDataSerializer.is_valid():
            aIFilteredDataSerializer.save()
            return JsonResponse(aIFilteredDataSerializer.data['AIFilteredDataId'], safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        aIFilteredDataData = JSONParser().parse(request)
        aIFilteredData = AIFilteredData.objects.get(
            AIFilteredDataId=aIFilteredDataData['AIFilteredDataId'])
        aIFilteredDataSerializer = AIFilteredDataSerializer(
            aIFilteredData, data=aIFilteredDataData)
        if aIFilteredDataSerializer.is_valid():
            aIFilteredDataSerializer.save()
            return JsonResponse("Update successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        # aIFilteredData = AIFilteredData.objects.get(
        #     AIFilteredDataId=pk)
        # aIFilteredData.delete()
        return JsonResponse("Deleted successfully", safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def mediaAdTypeWithMediaView(request):
    if request.method == 'post':
        post_data = JSONParser().parse(request)
        media_mediaadtype = connection.cursor()
        query=""
        if post_data['CountryId'] and len(post_data['CountryId']):
            sub_query=""
            for id in post_data['CountryId']:
                if sub_query:
                    sub_query=sub_query+ " OR "
                sub_query=sub_query+" JSON_CONTAINS(CountryEventJSON, '"+'"' + id+'"'+"') "
            query=query+" AND " +sub_query
        if post_data['VerticalId'] and len(post_data['VerticalId']):
            sub_query=""
            for id in post_data['VerticalId']:
                if sub_query:
                    sub_query=sub_query+ " OR "
                sub_query=sub_query+" VerticalType = '"+ id +"' "
            query=query+" AND (" +sub_query + ")"
        
        if query:
            query="WHERE "+query    
        media_mediaadtype.execute("SELECT * FROM MediaAdTypeWithMediaView " + query + ";")
        field_names = [i[0] for i in media_mediaadtype.description]
        media_mediaadtypeData = []
        for media in media_mediaadtype.fetchall():
            media_dict = dict(zip(field_names, media))
            media_mediaadtypeData.append(media_dict)

        MediaViewData = []
        batch_size = 1000
        
        countries = CountryEventSerializer(CountryEvent.objects.all(),many=True).data
        city_regions = CityRegionSerializer(CityRegion.objects.all(),many=True).data
        matching_categories = MatchingCategorySerializer(MatchingCategory.objects.all(),many=True).data
        languages = LanguageSerializer(Language.objects.all(),many=True).data
        media_categories = MediaCategorySerializer(MediaCategory.objects.all(),many=True).data
        Ad_Unit_Category = AdUnitCategorySerializer(AdUnitCategory.objects.all(),many=True).data
        for start in range(0, len(media_mediaadtypeData), batch_size):
            batch = media_mediaadtypeData[start:start + batch_size]


            for media in batch:
                AdUnitName = media['PackageName'] if media['MediaAdType'] == "Package" else media['SiteName']
                CityRegionD=[]
                CountryEventD=[]
                MatchingCategoriesD=[]
                LanguageD=[]
                try:
                    CityRegionD=json.loads(media['CityRegion'])
                except:
                    p=""
                try:
                    CountryEventD=json.loads(media['CountryEvent'])
                except:
                    p=""
                try:
                    MatchingCategoriesD=json.loads(media['MatchingCategories'])
                except:
                    p=""
                try:
                    LanguageD=json.loads(media['Language'])
                except:
                    p=""

                country_data = []
                city_region_data =[] 
                matching_categories_data = []
                language_data = []
                media_category_data = ""
                has_country=False
                for id in (CountryEventD or []):
                    for data in countries:
                        if data['CountryEventId']==id:
                            country_data.append(data['CountryEventName'])
                            has_country=True
                for id in (CityRegionD or []):
                    for data in city_regions:
                        if data['CityId']==id:
                            city_region_data.append(data['CityRegionName'])
                for id in (MatchingCategoriesD or []):
                    for data in matching_categories:
                        if data['MatchingCategoryId']==id:
                            matching_categories_data.append(data['MatchingCategory'])
                for id in (LanguageD or []):
                    for data in languages:
                        if data['LanguageId']==id:
                            language_data.append(data['Language'])
                for data in Ad_Unit_Category:
                    if data['AdUnitCategoryId']==media['MediaCategory']:
                        media_category_data=(data['AdUnitCategory'])
                if has_country:
                    MediaViewData.append({
                    'AdUnitName': AdUnitName,
                    'MediaAdTypeId': media['MediaAdTypeId'],
                    'MediaAdType': media['MediaAdType'],
                    'MediaName': media['MediaName'],
                    'ThumbnailImage': media['ThumbnailImage'],
                    'BenefitsOfAdvertising': media['BenefitsOfAdvertising'],
                    'MediaAdUnitDescriptionNonHTML': media['MediaAdUnitDescriptionNonHTML'],
                    'VerticalTypeName': media['VerticalTypeName'],
                    'VerticalType': media['VerticalType'],
                    'MediaId': media['MediaId'],
                    'LanguageName': media['LanguageName'],
                    'EstimatedReachName': media['EstimatedReachName'],
                    'MediaImage': media['MediaImage'],
                    'MediaManagedBy': media['MediaManagedBy'],
                    'AdUnitSpecificCategoryName': media['AdUnitSpecificCategoryName'],
                    'AdUnitCategoryName': media['AdUnitCategoryIdName'],
                    'CountryEventJSON': country_data,
                    'CountryEventIdJSON': CountryEventD,
                    'CityRegionIdJSON': CityRegionD,
                    'CityRegionJSON': city_region_data,
                    'MediaCategory': media['MediaCategory'],
                    'MediaCategoryName': media_category_data,
                    'MatchingCategoriesIdJSON': MatchingCategoriesD,
                    'MatchingCategoriesJSON': matching_categories_data,
                    'LanguageIdJSON': LanguageD,
                    'LanguageJSON': language_data,
                })

        return JsonResponse(MediaViewData, safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)

from django.db.models import Q
import json
import pandas as pd
from django.http import HttpResponse
from io import BytesIO


# Sample filter values
vertical_types = [
    '1166b5ee-a0a1-40b6-88b6-2713e0a058de',
    '4c21a24d-01eb-4995-b96f-973a58e72d77',
    '6f71ac89-03c9-4c99-8e54-d43fefaab1ef',
    'b195a568-0cc6-4a16-a552-761e795e854f'
]
media_categories = [
    '5ca8013a-97f9-431d-b62c-8640348b4ada',
    '7059141e-ae3d-420b-8952-0712ce30d912',
    '89777614-7cf3-4168-9705-950662568bac',
    'c37015bb-3a67-4808-ab7e-79186020f565'
]

def fetch_related_data():
    # Fetch only IDs for related tables (CountryEvent, CityRegion, etc.)
    country_event_query = CountryEvent.objects.all().values('CountryEventId', 'CountryEventName')
    city_region_query = CityRegion.objects.all().values('CityId', 'CityRegionName')
    language_query = Language.objects.all().values('LanguageId', 'Language')
    matching_category_query = MatchingCategory.objects.all().values('MatchingCategoryId', 'MatchingCategory')

    # Create dictionaries for fast lookup
    country_event_dict = {item['CountryEventId']: item['CountryEventName'] for item in country_event_query}
    city_region_dict = {item['CityId']: item['CityRegionName'] for item in city_region_query}
    language_dict = {item['LanguageId']: item['Language'] for item in language_query}
    matching_category_dict = {item['MatchingCategoryId']: item['MatchingCategory'] for item in matching_category_query}

    return country_event_dict, city_region_dict, language_dict, matching_category_dict

# Query the main data (no JSON extraction in the SQL)
def execute_raw_query():
    query = """
    SELECT 
        m.MediaAdTypeId, m.MediaAdType, m.PackageName, m.SiteName, m.MediaName, m.ThumbnailImage,
        m.MediaAdUnitDescriptionNonHTML, m.VerticalTypeName, m.VerticalType, m.MediaId, m.PriceRangeNote,
        m.CountryEventJSON, m.CityRegionJSON, m.LanguageJSON, m.LanguageName, m.EstimatedReachName, m.MediaImage,
        m.MediaCategory, m.MediaManagedBy, m.MatchingCategoriesJSON, m.AdUnitSpecificCategoryName, 
        m.RunAsOffer, m.NetCost, m.Currency, m.LocationType
    FROM MediaAdTypeWithMediaView AS m
    WHERE m.VerticalType IN ('1166b5ee-a0a1-40b6-88b6-2713e0a058de', 
                              '4c21a24d-01eb-4995-b96f-973a58e72d77', 
                              '6f71ac89-03c9-4c99-8e54-d43fefaab1ef', 
                              'b195a568-0cc6-4a16-a552-761e795e854f')
    AND m.MediaCategory IN ('5ca8013a-97f9-431d-b62c-8640348b4ada', 
                             '7059141e-ae3d-420b-8952-0712ce30d912', 
                             '89777614-7cf3-4168-9705-950662568bac', 
                             'c37015bb-3a67-4808-ab7e-79186020f565');
    """

    with connection.cursor() as cursor:
        cursor.execute(query)
        field_names = [i[0] for i in cursor.description]
        rows = cursor.fetchall()  # Fetch all rows

        media_mediaadtype_data = []
        for media in rows:
            media_ad_unit = {}
            for j, col in enumerate(media):
                if j < len(field_names):
                    media_ad_unit[str(field_names[j])] = col
            media_mediaadtype_data.append(media_ad_unit)

    return media_mediaadtype_data


# Fetch and process the data
def get_filtered_data(request):
    # Execute raw query and get the rows
    rows = execute_raw_query()

    # Fetch related data for fast lookup
    country_event_dict, city_region_dict, language_dict, matching_category_dict = fetch_related_data()

    # Process the result
    result = []
    for media_ad_unit in rows:
        # Get JSON data from the raw result
        country_event_json = media_ad_unit.get('CountryEventJSON', None)
        city_region_json = media_ad_unit.get('CityRegionJSON', None)
        language_json = media_ad_unit.get('LanguageJSON', None)
        matching_categories_json = media_ad_unit.get('MatchingCategoriesJSON', None)

        # Replace IDs with corresponding names from dictionaries
        country_event_name = None
        city_region_name = None
        language_name = None
        matching_category_name = None
        # Check if the JSON exists and is valid# Handle country_event_json (List of IDs)
        
        # Handle country_event_json (List of IDs)
        if country_event_json:
            try:
                country_event_data = json.loads(country_event_json)
                if isinstance(country_event_data, list):
                    country_event_names = [
                        country_event_dict.get(event_id, None) for event_id in country_event_data
                    ]
                    # Debug: Check which IDs are being mapped
                    country_event_name = ", ".join(filter(None, country_event_names))
            except json.JSONDecodeError:
                pass  # Handle any invalid JSON data

        # Handle city_region_json (List of IDs)
        if city_region_json:
            try:
                city_region_data = json.loads(city_region_json)
                if isinstance(city_region_data, list):
                    city_region_names = [
                        city_region_dict.get(region_id, None) for region_id in city_region_data
                    ]
                    city_region_name = ", ".join(filter(None, city_region_names))
            except json.JSONDecodeError:
                pass

        # Handle language_json (List of IDs)
        if language_json:
            try:
                language_data = json.loads(language_json)
                if isinstance(language_data, list):
                    language_names = [
                        language_dict.get(lang_id, None) for lang_id in language_data
                    ]
                    language_name = ", ".join(filter(None, language_names))
            except json.JSONDecodeError:
                pass

        # Handle matching_categories_json (List of IDs)
        if matching_categories_json:
            try:
                matching_categories_data = json.loads(matching_categories_json)
                if isinstance(matching_categories_data, list):
                    matching_category_names = [
                        matching_category_dict.get(cat_id, None) for cat_id in matching_categories_data
                    ]
                    matching_category_name = ", ".join(filter(None, matching_category_names))
            except json.JSONDecodeError:
                pass

        # Append processed data to result
        result.append({
            'MediaAdTypeId': media_ad_unit.get('MediaAdTypeId', None),
            'MediaAdType': media_ad_unit.get('MediaAdType', None),
            'PackageName': media_ad_unit.get('PackageName', None),
            'SiteName': media_ad_unit.get('SiteName', None),
            'MediaName': media_ad_unit.get('MediaName', None),
            'ThumbnailImage': media_ad_unit.get('ThumbnailImage', None),
            'MediaAdUnitDescriptionNonHTML': media_ad_unit.get('MediaAdUnitDescriptionNonHTML', None),
            'VerticalTypeName': media_ad_unit.get('VerticalTypeName', None),
            'VerticalType': media_ad_unit.get('VerticalType', None),
            'MediaId': media_ad_unit.get('MediaId', None),
            'PriceRangeNote': media_ad_unit.get('PriceRangeNote', None),
            'CountryEventName': country_event_name,
            'CityRegionName': city_region_name,
            'LanguageName': language_name,
            'MatchingCategoryName': matching_category_name,
            'LanguageName': media_ad_unit.get('LanguageName', None),
            'EstimatedReachName': media_ad_unit.get('EstimatedReachName', None),
            'MediaImage': media_ad_unit.get('MediaImage', None),
            'MediaCategory': media_ad_unit.get('MediaCategory', None),
            'MediaManagedBy': media_ad_unit.get('MediaManagedBy', None),
            'AdUnitSpecificCategoryName': media_ad_unit.get('AdUnitSpecificCategoryName', None),
            'RunAsOffer': media_ad_unit.get('RunAsOffer', None),
            'NetCost': media_ad_unit.get('NetCost', None),
            'Currency': media_ad_unit.get('Currency', None),
            'LocationType': media_ad_unit.get('LocationType', None),
        })

    # Return the result as a JSON response
    # return JsonResponse(result, safe=False)

    # Convert transformed data to DataFrame
    df = pd.DataFrame(result)

    # Create an Excel file
    excel_file = BytesIO()
    with pd.ExcelWriter(excel_file, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Filtered Data with Names")
    excel_file.seek(0)

    # Serve as a response
    response = HttpResponse(
        excel_file,
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
    response["Content-Disposition"] = "attachment; filename=filtered_data_with_names.xlsx"

    return response



