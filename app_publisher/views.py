from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from app_publisher.models import MeetingRequest, PublisherContact, PublisherRegister

from app_publisher.serializers import PublisherContactSerializer, PublisherRegisterSerializer, PublisherSerializer, SaveMeetingRequestSerializer, SavePublisherContactSerializer, SavePublisherSEOSerializer, SavePublisherSerializer, SavePublisherUrlSerializer, UploadPublisherBannerForMobileSerializer, UploadPublisherBannerSerializer, UploadPublisherContactSerializer, UploadPublisherSerializer

# Create your views here.

# "SELECT IFNULL(MediaCount, "0") as MediaCount, IFNULL(PublisherContactCount, "0") as PublisherContactCount,PublisherId FROM (SELECT media.*,app_publisher_publisherregister.PublisherId FROM (SELECT COUNT(`PublisherId`) as MediaCount,PublisherId as PM FROM `app_vertical_media_media` GROUP BY PublisherId ORDER BY PublisherId ASC) as media Right join `app_publisher_publisherregister` on media.PM=app_publisher_publisherregister.PublisherId ) as p_m_table LEFT JOIN (SELECT COUNT(`PublisherId`) as PublisherContactCount,PublisherId as PC FROM `app_publisher_publishercontact` GROUP BY PublisherId ORDER BY PublisherId ASC) as contact on contact.PC=p_m_table.PublisherId"


@csrf_exempt
def CURDPublisherMCCountApi(request, pk=""):
    try:
        if request.method == 'GET':
            cursor = connection.cursor()
            cursor.execute("SELECT IFNULL(MediaCount, '0') as MediaCount, IFNULL(PublisherContactCount, '0') as PublisherContactCount,PublisherId FROM (SELECT media.*,app_publisher_publisherregister.PublisherId FROM (SELECT COUNT(`PublisherId`) as MediaCount,PublisherId as PM FROM `app_vertical_media_media` GROUP BY PublisherId ORDER BY PublisherId ASC) as media Right join `app_publisher_publisherregister` on media.PM=app_publisher_publisherregister.PublisherId ) as p_m_table LEFT JOIN (SELECT COUNT(`PublisherId`) as PublisherContactCount,PublisherId as PC FROM `app_publisher_publishercontact` GROUP BY PublisherId ORDER BY PublisherId ASC) as contact on contact.PC=p_m_table.PublisherId")
            row = cursor.fetchall()
            # return row
            return JsonResponse(row, safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def PublisherDetailByUsername(request, UserName=""):
    try:
        if request.method == 'GET':
            profile = PublisherRegister.objects.get(
                UserName=UserName)
            profileSerializer = PublisherSerializer(
                profile)
            return JsonResponse(profileSerializer.data, safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDPublisherProfileApi(request, pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                profile = PublisherRegister.objects.all()
                profileSerializer = PublisherSerializer(
                    profile, many=True)
                return JsonResponse(profileSerializer.data, safe=False)
            else:
                profile = PublisherRegister.objects.get(
                    PublisherId=pk)
                profileSerializer = PublisherSerializer(
                    profile)
                return JsonResponse(profileSerializer.data, safe=False)
        elif request.method == 'POST':
            profileData = JSONParser().parse(request)
            # return JsonResponse(profileData, safe=False)
            profileSerializer = SavePublisherSerializer(
                data=profileData)
            if profileSerializer.is_valid():
                profileSerializer.save()
                return JsonResponse(profileSerializer.data['PublisherId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            profileData = JSONParser().parse(request)
            profile = PublisherRegister.objects.get(
                PublisherId=profileData['PublisherId'])
            profileSerializer = SavePublisherSerializer(
                profile, data=profileData)
            if profileSerializer.is_valid():
                profileSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            profile = PublisherRegister.objects.get(
                PublisherId=pk)
            PublisherRegister.objects.get(
                PublisherId=pk).BannerImage.delete(save=True)
            PublisherRegister.objects.get(
                PublisherId=pk).ProfileImage.delete(save=True)
            profile.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDPublisherProfileURlApi(request, pk=""):
    try:
        if request.method == 'PUT':
            profileData = JSONParser().parse(request)
            profile = PublisherRegister.objects.get(
                PublisherId=profileData['PublisherId'])
            profileSerializer = SavePublisherUrlSerializer(
                profile, data=profileData)
            if profileSerializer.is_valid():
                profileSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDPublisherProfileSEOApi(request, pk=""):
    # try:
        if request.method == 'PUT':
            profileData = JSONParser().parse(request)
            profile = PublisherRegister.objects.get(
                PublisherId=profileData['PublisherId'])
            profileSerializer = SavePublisherSEOSerializer(
                profile, data=profileData)
            if profileSerializer.is_valid():
                profileSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDPublisherRegisterApi(request, pk=""):
    try:
        if request.method == 'POST':
            profileData = JSONParser().parse(request)
            # return JsonResponse(profileData, safe=False)
            profileSerializer = PublisherRegisterSerializer(
                data=profileData)
            if profileSerializer.is_valid():
                profileSerializer.save()
                return JsonResponse(profileSerializer.data['PublisherId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


class UploadPublisherProfileFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, pk="", *args, **kwargs):
        try:
            if not pk:
                file_serializer = UploadPublisherSerializer(data=request.data)
                if file_serializer.is_valid():
                    file_serializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse("failed", safe=False)
            else:
                publisherRegister = PublisherRegister.objects.get(
                    PublisherId=pk)
                PublisherRegister.objects.get(
                    PublisherId=pk).ProfileImage.delete(save=True)
                uploadPublisherSerializer = UploadPublisherSerializer(
                    publisherRegister, data=request.data)
                if uploadPublisherSerializer.is_valid():
                    uploadPublisherSerializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse(pk, safe=False)
        except:
            return JsonResponse("Invalid payload", safe=False)


class UploadPublisherSeoBannerFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, pk="", *args, **kwargs):
        try:
            if not pk:
                file_serializer = UploadPublisherBannerSerializer(
                    data=request.data)
                if file_serializer.is_valid():
                    file_serializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse("failed", safe=False)
            else:
                publisherRegister = PublisherRegister.objects.get(
                    PublisherId=pk)
                PublisherRegister.objects.get(
                    PublisherId=pk).BannerImage.delete(save=True)
                uploadPublisherSerializer = UploadPublisherBannerSerializer(
                    publisherRegister, data=request.data)
                if uploadPublisherSerializer.is_valid():
                    uploadPublisherSerializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse(pk, safe=False)
        except:
            return JsonResponse("Invalid payload", safe=False)


class UploadPublisherSeoBannerForMoblieFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, pk="", *args, **kwargs):
        try:
            if not pk:
                file_serializer = UploadPublisherBannerForMobileSerializer(
                    data=request.data)
                if file_serializer.is_valid():
                    file_serializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse("failed", safe=False)
            else:
                publisherRegister = PublisherRegister.objects.get(
                    PublisherId=pk)
                PublisherRegister.objects.get(
                    PublisherId=pk).BannerImage.delete(save=True)
                uploadPublisherSerializer = UploadPublisherBannerForMobileSerializer(
                    publisherRegister, data=request.data)
                if uploadPublisherSerializer.is_valid():
                    uploadPublisherSerializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse(pk, safe=False)
        except:
            return JsonResponse("Invalid payload", safe=False)



@csrf_exempt
def CURDPublisherContactApi(request, PublisherId="", pk=""):
    # return JsonResponse(request.method, safe=False)
    # try:
    if request.method == 'GET':
        if not pk and PublisherId:
            publisherContact = PublisherContact.objects.filter(
                PublisherId=PublisherId)
            publisherContactSerializer = PublisherContactSerializer(
                publisherContact, many=True)
            return JsonResponse(publisherContactSerializer.data, safe=False)
        elif pk:
            publisherContact = PublisherContact.objects.get(
                PublisherContactId=pk)
            publisherContactSerializer = PublisherContactSerializer(
                publisherContact)
            return JsonResponse(publisherContactSerializer.data, safe=False)
        else:
            publisherContact = PublisherContact.objects.all()
            publisherContactSerializer = PublisherContactSerializer(
                publisherContact, many=True)
            return JsonResponse(publisherContactSerializer.data, safe=False)
    elif request.method == 'POST':
        publisherContactData = JSONParser().parse(request)
        publisherContactSerializer = SavePublisherContactSerializer(
            data=publisherContactData)
        if publisherContactSerializer.is_valid():
            publisherContactSerializer.save()
            return JsonResponse(publisherContactSerializer.data['PublisherContactId'], safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        publisherContactData = JSONParser().parse(request)
        publisherContact = PublisherContact.objects.get(
            PublisherContactId=publisherContactData['PublisherContactId'])
        publisherContactSerializer = SavePublisherContactSerializer(
            publisherContact, data=publisherContactData)
        if publisherContactSerializer.is_valid():
            publisherContactSerializer.save()
            return JsonResponse("Update successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        publisherContact = PublisherContact.objects.get(
            PublisherContactId=pk)
        publisherContact.ProfileImage.delete(save=True)
        publisherContact.delete()
        return JsonResponse("Deleted successfully", safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


class PublisherContactFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, pk="", *args, **kwargs):
        try:
            if not pk:
                file_serializer = UploadPublisherContactSerializer(
                    data=request.data)
                if file_serializer.is_valid():
                    file_serializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse("failed", safe=False)
            else:
                publisherContact = PublisherContact.objects.get(
                    PublisherContactId=pk)
                publisherContactSerializer = UploadPublisherContactSerializer(
                    publisherContact, data=request.data)
                if publisherContactSerializer.is_valid():
                    publisherContactSerializer.save()
                    return JsonResponse("ok", safe=False)
                else:
                    return JsonResponse(pk, safe=False)
        except:
            return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDMeetingRequestApi(request, PublisherId="", pk=""):
    # return JsonResponse(request.method, safe=False)
    # try:
    if request.method == 'GET':
        if not pk and PublisherId:
            meetingRequest = MeetingRequest.objects.filter(
                PublisherId=PublisherId)
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
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDMeetingRequestByAdvertiserApi(request, AdvertiserId="", pk=""):
    # return JsonResponse(request.method, safe=False)
    # try:
    if request.method == 'GET':
        if not pk:
            meetingRequest = MeetingRequest.objects.filter(
                AdvertiserId=AdvertiserId)
            saveMeetingRequestSerializer = SaveMeetingRequestSerializer(
                meetingRequest, many=True)
            return JsonResponse(saveMeetingRequestSerializer.data, safe=False)
        else:
            meetingRequest = MeetingRequest.objects.get(
                MeetingRequestId=pk)
            saveMeetingRequestSerializer = SaveMeetingRequestSerializer(
                meetingRequest)
            return JsonResponse(saveMeetingRequestSerializer.data, safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDMeetingRequestAdvertiserMedia(request, MediaId="", AdvertiserId=""):
    # return JsonResponse(request.method, safe=False)
    # try:
    if request.method == 'GET':
        meetingRequest = MeetingRequest.objects.filter(
            AdvertiserId=AdvertiserId, MediaId=MediaId)
        saveMeetingRequestSerializer = SaveMeetingRequestSerializer(
            meetingRequest, many=True)
        return JsonResponse(saveMeetingRequestSerializer.data, safe=False)
    else:
        return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)
