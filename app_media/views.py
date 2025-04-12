import calendar
import datetime
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from app_media.models import CampaignReportDetail, CampaignReportRegister, Cart, EstimateShorten, Plan, PlanDetail

from app_media.serializers import CampaignReportDetailSerializer, CampaignReportRegisterSerializer, CartSerializer, EstimateShortenSerializer, PlanDetailSerializer, PlanSerializer, SaveCampaignReportRegisterSerializer, UploadCampaignReportRegisterSerializer, ViewPlanSerializer
from app_vertical_media.models import Media
from app_vertical_media.serializers import MediaSerializer

# Create your views here.
import json


@csrf_exempt
def CURDCartRecommendedMediaApi(request, userId="", CartType="", pk=""):
    # try:
    if request.method == 'GET':
        if not pk:
            cart = Cart.objects.filter(
                AdvertiserId=userId, CartType=CartType)
            cartSerializer = CartSerializer(
                cart, many=True)
            adUnitId = ""
            for cart in cartSerializer.data:
                if adUnitId:
                    adUnitId = adUnitId+","
                adUnitId = adUnitId + "'"+cart['MediaAdTypeId'] + "'"

            media = Media.objects.raw(
                "SELECT * FROM `app_vertical_media_media` WHERE app_vertical_media_media.`MediaId` IN (SELECT app_vertical_media_mediaadtype.MediaId FROM app_vertical_media_mediaadtype WHERE app_vertical_media_mediaadtype.MediaAdTypeId IN ("+adUnitId+"))")
            mediaSerializer = MediaSerializer(
                media, many=True)
            mediaId = ""
            for mediaSeri in mediaSerializer.data:
                RecommendedMedia = []
                if mediaSeri['RecommendedMedia']:
                    RecommendedMedia = json.loads(
                        mediaSeri['RecommendedMedia'])
                for medi in RecommendedMedia:
                    if mediaId:
                        mediaId = mediaId+","
                    mediaId = mediaId + "'"+medi + "'"
            media = Media.objects.raw(
                "SELECT * FROM `app_vertical_media_media` WHERE `MediaId` IN ("+mediaId+")")
            mediaSerializer = MediaSerializer(
                media, many=True)
            # return JsonResponse("SELECT * FROM `app_vertical_media_media` WHERE app_vertical_media_media.`MediaId` IN (SELECT app_vertical_media_mediaadtype.MediaId FROM app_vertical_media_mediaadtype WHERE app_vertical_media_mediaadtype.MediaAdTypeId IN ("+adUnitId+"))", safe=False)

            return JsonResponse(mediaSerializer.data, safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDCartApi(request, userId="", CartType="", pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                cart = Cart.objects.filter(
                    AdvertiserId=userId, CartType=CartType)
                cartSerializer = CartSerializer(
                    cart, many=True)
                return JsonResponse(cartSerializer.data, safe=False)
            else:
                cart = Cart.objects.get(
                    AdvertiserId=userId, CartId=pk, CartType=CartType)
                cartSerializer = CartSerializer(
                    cart)
                return JsonResponse(cartSerializer.data, safe=False)
        elif request.method == 'POST':
            cartData = JSONParser().parse(request)
            # return JsonResponse(cartData, safe=False)
            cartSerializer = CartSerializer(
                data=cartData)
            if cartSerializer.is_valid():
                cartSerializer.save()
                return JsonResponse(cartSerializer.data['CartId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            cartData = JSONParser().parse(request)
            cart = Cart.objects.get(
                CartId=cartData['CartId'])
            cartSerializer = CartSerializer(
                cart, data=cartData)
            if cartSerializer.is_valid():
                cartSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            cart = Cart.objects.get(
                CartId=pk)
            cart.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDPlanApi(request, userId="", pk=""):
    # try:
    if request.method == 'GET':
        if pk:
            plan = Plan.objects.get(
                PlanId=pk)
            planSerializer = ViewPlanSerializer(
                plan)
            return JsonResponse(planSerializer.data, safe=False)
        elif userId:
            plan = Plan.objects.filter(
                AdvertiserId=userId)
            planSerializer = ViewPlanSerializer(
                plan, many=True)
            return JsonResponse(planSerializer.data, safe=False)
        else:
            plan = Plan.objects.all()
            planListSerializer = ViewPlanSerializer(plan, many=True)
            return JsonResponse(planListSerializer.data, safe=False)
    elif request.method == 'POST':
        planData = JSONParser().parse(request)
        # return JsonResponse(planData, safe=False)
        planSerializer = PlanSerializer(
            data=planData)
        if planSerializer.is_valid():
            planSerializer.save()
            return JsonResponse(planSerializer.data['PlanId'], safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        planData = JSONParser().parse(request)
        plan = Plan.objects.get(
            PlanId=planData['PlanId'])
        planSerializer = PlanSerializer(
            plan, data=planData)
        if planSerializer.is_valid():
            planSerializer.save()
            return JsonResponse("Update successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        plan = Plan.objects.get(
            PlanId=pk)
        plan.delete()
        return JsonResponse("Deleted successfully", safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDPlanByPublisher(request, userId=""):
    # try:
    if request.method == 'GET':
        if userId:
            plan = Plan.objects.raw(
                "SELECT * FROM `app_media_plan` WHERE `Status`<>'0' AND `PlanId` IN (SELECT `PlanId` FROM `app_media_plandetail` WHERE `Status`<>'0' AND  `app_media_plandetail`.MediaDetail  LIKE '%%" + userId + "%%')")
            planSerializer = ViewPlanSerializer(
                plan, many=True)
            return JsonResponse(planSerializer.data, safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDPlanByAdmin(request):
    # try:
    if request.method == 'GET':
        plan = Plan.objects.raw(
            "SELECT * FROM `app_media_plan` WHERE `Status`<>'0'")
        planSerializer = ViewPlanSerializer(
            plan, many=True)
        return JsonResponse(planSerializer.data, safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDPlanDetailApi(request, planId="", AdvertiserId="", pk=""):
    # try:
    if request.method == 'GET':
        if pk:
            planDetail = PlanDetail.objects.get(
                PlanDetailId=pk)
            planDetailSerializer = PlanDetailSerializer(
                planDetail)
            return JsonResponse(planDetailSerializer.data, safe=False)
        elif AdvertiserId:
            planDetail = PlanDetail.objects.filter(
                AdvertiserId=AdvertiserId, PlanId=planId)
            planDetailSerializer = PlanDetailSerializer(
                planDetail, many=True)
            return JsonResponse(planDetailSerializer.data, safe=False)
        else:
            planDetail = PlanDetail.objects.filter(
                PlanId=planId)
            planDetailSerializer = PlanDetailSerializer(
                planDetail, many=True)
            return JsonResponse(planDetailSerializer.data, safe=False)
    elif request.method == 'POST':
        planDetailData = JSONParser().parse(request)
        planDetailSerializer = PlanDetailSerializer(
            data=planDetailData)
        if planDetailSerializer.is_valid():
            planDetailSerializer.save()
            return JsonResponse(planDetailSerializer.data['PlanDetailId'], safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        planDetailData = JSONParser().parse(request)
        planDetail = PlanDetail.objects.get(
            PlanDetailId=planDetailData['PlanDetailId'])
        planDetailSerializer = PlanDetailSerializer(
            planDetail, data=planDetailData)
        if planDetailSerializer.is_valid():
            planDetailSerializer.save()
            return JsonResponse(planDetailSerializer.data['PlanDetailId'], safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        if not pk:
            planDetail = PlanDetail.objects.filter(
                PlanId=planId, AdvertiserId=AdvertiserId)
            planDetail.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            planDetail = PlanDetail.objects.get(
                PlanDetailId=pk)
            planDetail.delete()
            return JsonResponse("Deleted successfully", safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDPlanDetailByPublisher(request, userId="", planId=""):
    # try:
    if request.method == 'GET':
        if planId:
            planDetail = PlanDetail.objects.raw(
                "SELECT * FROM `app_media_plandetail` WHERE `Status`<>'0' AND `app_media_plandetail`.MediaDetail  LIKE '%%" + userId + "%%' AND PlanId='" + planId + "'")
            planDetailSerializer = PlanDetailSerializer(
                planDetail, many=True)
            return JsonResponse(planDetailSerializer.data, safe=False)
        elif userId:
            plan = PlanDetail.objects.raw(
                "SELECT * FROM `app_media_plandetail` WHERE `Status`<>'0' AND `app_media_plandetail`.MediaDetail  LIKE '%%" + userId + "%%'")
            planSerializer = PlanDetailSerializer(
                plan, many=True)
            return JsonResponse(planSerializer.data, safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDPlanDetailByAdmin(request, userId="", planId=""):
    # try:
    if request.method == 'GET':
        if planId:
            planDetail = PlanDetail.objects.raw(
                "SELECT * FROM `app_media_plandetail` WHERE `Status`<>'0'")
            planDetailSerializer = PlanDetailSerializer(
                planDetail, many=True)
            return JsonResponse(planDetailSerializer.data, safe=False)
        elif userId:
            plan = PlanDetail.objects.raw(
                "SELECT * FROM `app_media_plandetail` WHERE `Status`<>'0'")
            planSerializer = PlanDetailSerializer(
                plan, many=True)
            return JsonResponse(planSerializer.data, safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def PlanEstimateShortenApi(request, UserId="", PlanId=""):
    try:
        if request.method == 'POST':
            if UserId and PlanId:
                estimateShorten = EstimateShorten.objects.get(
                    AdvertiserId=UserId, PlanId=PlanId)
                estimateShortenSerializer = EstimateShortenSerializer(
                    estimateShorten)
                return JsonResponse(estimateShortenSerializer.data['EstimateShortenId'], safe=False)

            else:
                return JsonResponse("", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        estimateShortenData = JSONParser().parse(request)
        estimateShortenSerializer = EstimateShortenSerializer(
            data=estimateShortenData)
        if estimateShortenSerializer.is_valid():
            estimateShortenSerializer.save()
            return JsonResponse(estimateShortenSerializer.data['EstimateShortenId'], safe=False)
        return JsonResponse("", safe=False)


@csrf_exempt
def CURDPlanEstimateShortenApi(request, pk=""):
    try:
        if request.method == 'GET':
            if pk:
                estimateShorten = EstimateShorten.objects.get(
                    EstimateShortenId=pk)
                estimateShortenSerializer = EstimateShortenSerializer(
                    estimateShorten)
                return JsonResponse(estimateShortenSerializer.data, safe=False)
            else:
                return JsonResponse("", safe=False)
        elif request.method == 'POST':
            estimateShortenData = JSONParser().parse(request)
            estimateShortenSerializer = EstimateShortenSerializer(
                data=estimateShortenData)
            if estimateShortenSerializer.is_valid():
                estimateShortenSerializer.save()
                return JsonResponse(estimateShortenSerializer.data['EstimateShortenId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("", safe=False)


@csrf_exempt
def dashboardDataForPublisher(request, PublisherId=""):
    # try:
    if request.method == 'GET':
        # vertical - media count start
        verticalCursor = connection.cursor()
        verticalCursor.execute(
            "SELECT `VerticalId`,`VerticalName` FROM `app_default_vertical` WHERE `RefId`=''")
        verticalRow = verticalCursor.fetchall()
        VerticalCount = []
        Data = []
        for x in verticalRow:
            verticalMediaCursor = connection.cursor()
            verticalMediaCursor.execute("SELECT COUNT(`Vertical`) as EnquiryCount,`Vertical` FROM `app_media_plandetail` WHERE " +
                                        "`Vertical`='"+x[0]+"' AND " +
                                        " `MediaDetail`  LIKE '%%" + PublisherId + "%%'")
            verticalMediaRow = verticalMediaCursor.fetchall()
            Vertical = []
            Vertical.append(x[1])
            # Vertical.append(verticalMediaRow[0][0])
            Vertical.append(verticalMediaRow[0][0])
            Data.append(Vertical)
        VerticalCount.append(Data)
        # vertical - media count end

        # last 3 month plan count count start
        AllDate = []
        today = sub_months(datetime.date.today(), 2)
        d = []
        d.append(today.strftime('%Y%m'))
        d.append(today.strftime('%Y'))
        d.append(today.strftime('%b'))
        AllDate.append(d)
        d = []
        d.append(add_months(today, 1).strftime('%Y%m'))
        d.append(add_months(today, 1).strftime('%Y'))
        d.append(add_months(today, 1).strftime('%b'))
        AllDate.append(d)
        d = []
        d.append(add_months(today, 2).strftime('%Y%m'))
        d.append(add_months(today, 2).strftime('%Y'))
        d.append(add_months(today, 2).strftime('%b'))
        AllDate.append(d)
        Data = []
        for date in AllDate:

            PlanCursor = connection.cursor()
            PlanCursor.execute("SELECT COUNT(`PlanDetailId`) FROM `app_media_plandetail` WHERE `Status` AND " +
                               " `MediaDetail`  LIKE '%%" + PublisherId + "%%'")
            PlanRow = PlanCursor.fetchall()
            MediaDateCount = []
            MediaDateCount.append(date)
            MediaDateCount.append(PlanRow[0][0])
            Data.append(MediaDateCount)
        VerticalCount.append(Data)
        # last 3 month plan count count end

        # Most viewed media start

        mediaCountCursor = connection.cursor()
        mediaCountCursor.execute(
            "SELECT * FROM `app_vertical_media_media` WHERE `PublisherId`='" + PublisherId + "' order by `ViewsCount` DESC LIMIT 4")
        mediaCountRow = mediaCountCursor.fetchall()
        VerticalCount.append(mediaCountRow)

        # Most viewed media end

        # Plan - approval , booking etc.. count start

        PlanCursor = connection.cursor()
        PlanCursor.execute("SELECT * FROM " +
                           " (SELECT COUNT(`PlanDetailId`) AS ApprovalPending FROM `app_media_plandetail` WHERE `Status`=1 AND  `MediaDetail`  LIKE '%%" + PublisherId + "%%') as ApprovalPending JOIN  " +
                           " (SELECT COUNT(`PlanDetailId`) as Confirmed FROM `app_media_plandetail` WHERE `Status`=3 AND  `MediaDetail`  LIKE '%%" + PublisherId + "%%') as Confirmed JOIN " +
                           " (SELECT COUNT(`PlanDetailId`) as Booked FROM `app_media_plandetail` WHERE `Status`=4 AND  `MediaDetail`  LIKE '%%" + PublisherId + "%%') as Booked")
        PlanRow = PlanCursor.fetchall()
        VerticalCount.append(PlanRow[0])

        # Plan - approval , booking etc.. count end

        return JsonResponse(VerticalCount, safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)


def sub_months(sourcedate, months):
    month = sourcedate.month - 1 - months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)


@csrf_exempt
def allPlanDetails(request):

    PlanCursor = connection.cursor()
    PlanCursor.execute("SELECT * FROM  " +
                       "(SELECT COUNT(`PlanId`) AS Draft FROM `app_media_plan` WHERE `Status`=0 ) as Draft JOIN   " +
                       "(SELECT COUNT(`PlanDetailId`) AS PublisherConfirmation FROM `app_media_plandetail` WHERE `Status`=1 ) as PublisherConfirmation JOIN   " +
                       "(SELECT COUNT(`PlanDetailId`) as AdvertiserConfirmation FROM `app_media_plandetail` WHERE `Status`=2 ) as AdvertiserConfirmation JOIN  " +
                       "(SELECT COUNT(`PlanDetailId`) as Confirmed FROM `app_media_plandetail` WHERE `Status`=3 ) as Confirmed JOIN   " +
                       "(SELECT COUNT(`PlanDetailId`) as Booked FROM `app_media_plandetail` WHERE `Status`=4 ) as Booked JOIN  " +
                       "(SELECT COUNT(`PlanDetailId`) as OnLive FROM `app_media_plandetail` WHERE `Status`=5 ) as OnLive JOIN  " +
                       "(SELECT COUNT(`PlanDetailId`) as Cancelled FROM `app_media_plandetail` WHERE `Status`=-1 ) as Cancelled")
    PlanRow = PlanCursor.fetchall()
    return JsonResponse(PlanRow[0], safe=False)


@csrf_exempt
def advertiserPlanDetails(request, AdvertiserId=""):

    PlanCursor = connection.cursor()
    PlanCursor.execute("SELECT * FROM  " +
                       "(SELECT COUNT(`PlanId`) AS Draft FROM `app_media_plan` WHERE `Status`=0 AND `AdvertiserId` = '" + AdvertiserId + "') as Draft JOIN   " +
                       "(SELECT COUNT(`PlanDetailId`) AS PublisherConfirmation FROM `app_media_plandetail` WHERE `Status`=1 AND `AdvertiserId` = '" + AdvertiserId + "') as PublisherConfirmation JOIN   " +
                       "(SELECT COUNT(`PlanDetailId`) as AdvertiserConfirmation FROM `app_media_plandetail` WHERE `Status`=2 AND `AdvertiserId` = '" + AdvertiserId + "') as AdvertiserConfirmation JOIN  " +
                       "(SELECT COUNT(`PlanDetailId`) as Confirmed FROM `app_media_plandetail` WHERE `Status`=3 AND `AdvertiserId` = '" + AdvertiserId + "') as Confirmed JOIN   " +
                       "(SELECT COUNT(`PlanDetailId`) as Booked FROM `app_media_plandetail` WHERE `Status`=4 AND `AdvertiserId` = '" + AdvertiserId + "') as Booked JOIN  " +
                       "(SELECT COUNT(`PlanDetailId`) as OnLive FROM `app_media_plandetail` WHERE `Status`=5 AND `AdvertiserId` = '" + AdvertiserId + "') as OnLive JOIN  " +
                       "(SELECT COUNT(`PlanDetailId`) as Cancelled FROM `app_media_plandetail` WHERE `Status`=-1 AND `AdvertiserId` = '" + AdvertiserId + "') as Cancelled")
    PlanRow = PlanCursor.fetchall()
    return JsonResponse(PlanRow[0], safe=False)


@csrf_exempt
def publisherPlanDetails(request, PublisherId=""):

    PlanCursor = connection.cursor()
    PlanCursor.execute("SELECT * FROM  " +
                       "(SELECT COUNT(`PlanDetailId`) AS Draft FROM `app_media_plandetail` WHERE `Status`=0 AND   `MediaDetail`  LIKE '%%" + PublisherId + "%%') as Draft JOIN   " +
                       "(SELECT COUNT(`PlanDetailId`) AS PublisherConfirmation FROM `app_media_plandetail` WHERE `Status`=1 AND   `MediaDetail`  LIKE '%%" + PublisherId + "%%') as PublisherConfirmation JOIN   " +
                       "(SELECT COUNT(`PlanDetailId`) as AdvertiserConfirmation FROM `app_media_plandetail` WHERE `Status`=2 AND  `MediaDetail`  LIKE '%%" + PublisherId + "%%') as AdvertiserConfirmation JOIN  " +
                       "(SELECT COUNT(`PlanDetailId`) as Confirmed FROM `app_media_plandetail` WHERE `Status`=3 AND  `MediaDetail`  LIKE '%%" + PublisherId + "%%') as Confirmed JOIN   " +
                       "(SELECT COUNT(`PlanDetailId`) as Booked FROM `app_media_plandetail` WHERE `Status`=4 AND  `MediaDetail`  LIKE '%%" + PublisherId + "%%') as Booked JOIN  " +
                       "(SELECT COUNT(`PlanDetailId`) as OnLive FROM `app_media_plandetail` WHERE `Status`=5 AND  `MediaDetail`  LIKE '%%" + PublisherId + "%%') as OnLive JOIN  " +
                       "(SELECT COUNT(`PlanDetailId`) as Cancelled FROM `app_media_plandetail` WHERE `Status`=-1 AND  `MediaDetail`  LIKE '%%" + PublisherId + "%%') as Cancelled")
    PlanRow = PlanCursor.fetchall()
    return JsonResponse(PlanRow[0], safe=False)


@csrf_exempt
def dashboardDataForAdvertiser(request, AdvertiserId=""):
    # try:
    if request.method == 'GET':
        # vertical - media count start
        verticalCursor = connection.cursor()
        verticalCursor.execute(
            "SELECT `VerticalId`,`VerticalName` FROM `app_default_vertical` WHERE `RefId`=''")
        verticalRow = verticalCursor.fetchall()
        VerticalCount = []
        Data = []
        for x in verticalRow:
            verticalMediaCursor = connection.cursor()
            verticalMediaCursor.execute("SELECT COUNT(`Vertical`) as EnquiryCount,`Vertical` FROM `app_media_plandetail` WHERE " +
                                        "`Vertical`='"+x[0]+"' AND " +
                                        " `AdvertiserId` = '" + AdvertiserId + "'")
            verticalMediaRow = verticalMediaCursor.fetchall()
            Vertical = []
            Vertical.append(x[1])
            # Vertical.append(verticalMediaRow[0][0])
            Vertical.append(verticalMediaRow[0][0])
            Data.append(Vertical)
        VerticalCount.append(Data)
        # vertical - media count end

        # last 3 month plan count count start
        AllDate = []
        today = sub_months(datetime.date.today(), 2)
        d = []
        d.append(today.strftime('%Y%m'))
        d.append(today.strftime('%Y'))
        d.append(today.strftime('%b'))
        AllDate.append(d)
        d = []
        d.append(add_months(today, 1).strftime('%Y%m'))
        d.append(add_months(today, 1).strftime('%Y'))
        d.append(add_months(today, 1).strftime('%b'))
        AllDate.append(d)
        d = []
        d.append(add_months(today, 2).strftime('%Y%m'))
        d.append(add_months(today, 2).strftime('%Y'))
        d.append(add_months(today, 2).strftime('%b'))
        AllDate.append(d)
        Data = []
        for date in AllDate:

            PlanCursor = connection.cursor()
            PlanCursor.execute("SELECT  COUNT(`PlanId`)  FROM `app_media_plan` WHERE DATE_FORMAT(`SortId`,'%Y%m')='" + str(date[0]) + "' AND " +
                               " `AdvertiserId` = '" + AdvertiserId + "'")
            PlanRow = PlanCursor.fetchall()
            MediaDateCount = []
            MediaDateCount.append(date)
            MediaDateCount.append(PlanRow[0][0])
            Data.append(MediaDateCount)
        VerticalCount.append(Data)

        # last 3 month plan count count end

        # Plan - approval , booking etc.. count start

        PlanCursor = connection.cursor()
        PlanCursor.execute("SELECT * FROM " +
                           " (SELECT COUNT(`PlanId`) AS Draft FROM `app_media_plan` WHERE `Status`=0 AND  `AdvertiserId` = '" + AdvertiserId + "') as Draft JOIN  " +
                           " (SELECT COUNT(`PlanDetailId`) AS ApprovalPending FROM `app_media_plandetail` WHERE `Status`=1 AND  `AdvertiserId` = '" + AdvertiserId + "') as ApprovalPending JOIN  " +
                           " (SELECT COUNT(`PlanDetailId`) as Confirmed FROM `app_media_plandetail` WHERE `Status`=3 AND   `AdvertiserId` = '" + AdvertiserId + "') as Confirmed JOIN " +
                           " (SELECT COUNT(`PlanDetailId`) as Booked FROM `app_media_plandetail` WHERE `Status`=4 AND  `AdvertiserId` = '" + AdvertiserId + "') as Booked")
        PlanRow = PlanCursor.fetchall()
        VerticalCount.append(PlanRow[0])
        Data2 = []
        for date in AllDate:

            PlanCursor = connection.cursor()
            PlanCursor.execute("SELECT  COUNT(`PlanDetailId`)  FROM `app_media_plandetail` WHERE DATE_FORMAT(`SortId`,'%Y%m')='" + str(date[0]) + "' AND " +
                               " `AdvertiserId` = '" + AdvertiserId + "'")
            PlanRow = PlanCursor.fetchall()
            MediaDateCount = []
            MediaDateCount.append(date)
            MediaDateCount.append(PlanRow[0][0])
            Data2.append(MediaDateCount)
        VerticalCount.append(Data2)

        # Plan - approval , booking etc.. count end

        # return row
        return JsonResponse(VerticalCount, safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CampaignReport(request, PlanDetailId="", PlanId=""):
    if request.method == 'GET':
        campaignReportRegisters = CampaignReportRegister.objects.filter(
            PlanDetailId=PlanDetailId, PlanId=PlanId)
        campaignReportRegistersSerializer = CampaignReportRegisterSerializer(
            campaignReportRegisters, many=True)
        campaignReportRegisterData = []
        for ReportData in campaignReportRegistersSerializer.data:

            campaignReportDetails = CampaignReportDetail.objects.filter(
                CampaignReportRegisterId=ReportData['CampaignReportRegisterId'])
            campaignReportDetailsSerializer = CampaignReportDetailSerializer(
                campaignReportDetails, many=True)
            ReportData['CampaignReportDetail'] = campaignReportDetailsSerializer.data
            campaignReportRegisterData.append(ReportData)
        return JsonResponse(campaignReportRegisterData, safe=False)


@csrf_exempt
def CURDCampaignReportRegisterApi(request, pk=""):
    # try:
    if request.method == 'GET':
        if not pk:
            campaignReportRegisters = CampaignReportRegister.objects.all()
            campaignReportRegistersSerializer = CampaignReportRegisterSerializer(
                campaignReportRegisters, many=True)
            campaignReportRegisterData = []
            for ReportData in campaignReportRegistersSerializer.data:

                campaignReportDetails = CampaignReportDetail.objects.filter(
                    CampaignReportRegisterId=ReportData['CampaignReportRegisterId'])
                campaignReportDetailsSerializer = CampaignReportDetailSerializer(
                    campaignReportDetails, many=True)
                ReportData['CampaignReportDetail'] = campaignReportDetailsSerializer.data
                campaignReportRegisterData.append(ReportData)
            return JsonResponse(campaignReportRegisterData, safe=False)
        else:
            campaignReportRegisters = CampaignReportRegister.objects.get(
                CampaignReportRegisterId=pk)
            campaignReportRegistersSerializer = CampaignReportRegisterSerializer(
                campaignReportRegisters)
            return JsonResponse(campaignReportRegistersSerializer.data, safe=False)
    elif request.method == 'POST':
        campaignReportRegistersData = JSONParser().parse(request)
        campaignReportRegistersSerializer = SaveCampaignReportRegisterSerializer(
            data=campaignReportRegistersData)
        # campaignReportRegistersSerializer.is_valid()
        # return JsonResponse(campaignReportRegistersSerializer.data, safe=False)
        if campaignReportRegistersSerializer.is_valid():
            campaignReportRegistersSerializer.save()
            return JsonResponse(campaignReportRegistersSerializer.data['CampaignReportRegisterId'], safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        campaignReportRegistersData = JSONParser().parse(request)
        campaignReportRegisters = CampaignReportRegister.objects.get(
            CampaignReportRegisterId=campaignReportRegistersData['CampaignReportRegisterId'])
        campaignReportRegistersSerializer = SaveCampaignReportRegisterSerializer(
            campaignReportRegisters, data=campaignReportRegistersData)
        if campaignReportRegistersSerializer.is_valid():
            campaignReportRegistersSerializer.save()
            return JsonResponse("Update successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        campaignReportRegisters = CampaignReportRegister.objects.get(
            CampaignReportRegisterId=pk)
        campaignReportRegisters.delete()
        return JsonResponse("Deleted successfully", safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDCampaignReportDetailApi(request, pk=""):
    # try:
    if request.method == 'GET':
        if not pk:
            campaignReportDetails = CampaignReportDetail.objects.all()
            campaignReportDetailsSerializer = CampaignReportDetailSerializer(
                campaignReportDetails, many=True)
            return JsonResponse(campaignReportDetailsSerializer.data, safe=False)
        else:
            campaignReportDetails = CampaignReportDetail.objects.get(
                CampaignReportDetailId=pk)
            campaignReportDetailsSerializer = CampaignReportDetailSerializer(
                campaignReportDetails)
            return JsonResponse(campaignReportDetailsSerializer.data, safe=False)
    elif request.method == 'POST':
        campaignReportDetailsData = JSONParser().parse(request)
        campaignReportDetailsSerializer = CampaignReportDetailSerializer(
            data=campaignReportDetailsData)
        # campaignReportDetailsSerializer.is_valid()
        # return JsonResponse(campaignReportDetailsSerializer.data, safe=False)
        if campaignReportDetailsSerializer.is_valid():
            campaignReportDetailsSerializer.save()
            return JsonResponse(campaignReportDetailsSerializer.data['CampaignReportDetailId'], safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        campaignReportDetailsData = JSONParser().parse(request)
        campaignReportDetails = CampaignReportDetail.objects.get(
            CampaignReportDetailId=campaignReportDetailsData['CampaignReportDetailId'])
        campaignReportDetailsSerializer = CampaignReportDetailSerializer(
            campaignReportDetails, data=campaignReportDetailsData)
        if campaignReportDetailsSerializer.is_valid():
            campaignReportDetailsSerializer.save()
            return JsonResponse("Update successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        campaignReportDetails = CampaignReportDetail.objects.get(
            CampaignReportDetailId=pk)
        campaignReportDetails.delete()
        return JsonResponse("Deleted successfully", safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


class CampaignReportRegisterFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, pk="", *args, **kwargs):
        try:
            if not pk:
                file_serializer = UploadCampaignReportRegisterSerializer(
                    data=request.data)
                if file_serializer.is_valid():
                    file_serializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse("failed", safe=False)
            else:
                campaignReportRegisters = CampaignReportRegister.objects.get(
                    CampaignReportRegisterId=pk)
                CampaignReportRegister.objects.get(
                    CampaignReportRegisterId=pk).UploadProof.delete(save=True)
                campaignReportRegistersSerializer = UploadCampaignReportRegisterSerializer(
                    campaignReportRegisters, data=request.data)
                if campaignReportRegistersSerializer.is_valid():
                    campaignReportRegistersSerializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse(pk, safe=False)
        except:
            return JsonResponse("Invalid payload", safe=False)
