from datetime import datetime as dt
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from app_advertiser.models import Profile
from app_advertiser.serializers import ProfileSerializer, SaveProfileSerializer
from app_default.models import UserType
from app_default.serializers import UserTypeSerializer
from app_login.models import Login, UserTokenRegister
from app_login.serializers import LoginSerializer, LoginAuthSerializer, LoginSaveSerializer, LoginStatusSerializer, LoginUpdateSerializer, SocialLoginSerializer, UserTokenRegisterSerializer

# Create your views here.


@csrf_exempt
def loginApi(request, pk=""):
    # try:
    if request.method == 'GET':
        if not pk:
            # login = Login.objects.all()
            # login_serializer = LoginSerializer(login, many=True)
            # return JsonResponse(login_serializer.data, safe=False)
            return JsonResponse("", safe=False)
        else:
            login = Login.objects.get(LoginId=pk)
            login_serializer = LoginAuthSerializer(login)
            return JsonResponse(login_serializer.data, safe=False)
    elif request.method == 'POST':
        login_data = JSONParser().parse(request)
        login = Login.objects.filter(
            EmailId=login_data['EmailId'], Password=login_data['Password'], UserType=login_data['UserType'])
        Data = []
        login_serializer = LoginAuthSerializer(login, many=True)
        # return JsonResponse("login_serializer.data", safe=False)
        if not login_serializer.data:
            login = Login.objects.filter(
                EmailId=login_data['EmailId']).exclude(UserType=login_data['UserType'])
            login_serializer = LoginAuthSerializer(login, many=True)
            if not login_serializer.data:
                Data.append('FAILED')
                Data.append('')  # logindata
                Data.append('')  # token
                Data.append('')  # UserData
            else:
                Data.append('FAILED')
                Data.append(login_serializer.data[0])  # logindata
                Data.append('')  # token
                Data.append('')  # UserData
        else:
            UserToken_data = {}
            UserToken_data['EmailId'] = login_data['EmailId']
            UserToken_data['UserType'] = login_data['UserType']
            UserToken_data['LoginType'] = "Normal"
            UserToken_data['LoginId'] = login_serializer.data[0]['LoginId']

            UserToken_serializer = UserTokenRegisterSerializer(
                data=UserToken_data)
            if UserToken_serializer.is_valid():
                UserToken_serializer.save()
            Data.append('SUCCESS')
            Data.append(login_serializer.data[0])  # logindata
            Data.append(UserToken_serializer.data['TokenId'])  # token
            userType = UserType.objects.get(
                UserTypeId=login_serializer.data[0]['UserType'])
            userType_serializer = UserTypeSerializer(userType)
            if userType_serializer.data['UserType'] == 'Advertiser':
                profile = Profile.objects.get(
                    AdvertiserId=login_serializer.data[0]['UserId'])
                profileSerializer = ProfileSerializer(
                    profile)
                Data.append(profileSerializer.data)  # UserData
            else:
                Data.append('')  # UserData
        return JsonResponse(Data, safe=False)
    elif request.method == 'PUT':
        login_data = JSONParser().parse(request)
        login = Login.objects.get(
            EmailId=login_data['EmailId'], UserType=login_data['UserType'])
        login_serializer = LoginUpdateSerializer(login, data=login_data)
        if login_serializer.is_valid():
            login_serializer.save()
            return JsonResponse("Update successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)
    elif request.method == 'DELETE':
        login = Login.objects.get(LoginId=pk)
        login.delete()
        return JsonResponse("Deleted successfully", safe=False)

    # except:
    #     return JsonResponse("", safe=False)


@csrf_exempt
def GetLoginApi(request, UserId=""):
    try:
        if request.method == 'GET':
            if UserId:
                login = Login.objects.get(UserId=UserId)
                login_serializer = LoginAuthSerializer(login)
                return JsonResponse(login_serializer.data, safe=False)
            else:
                return JsonResponse("", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("", safe=False)


@csrf_exempt
def GetLoginByLoginIdApi(request, LoginId=""):
    try:
        if request.method == 'GET':
            if LoginId:
                login = Login.objects.get(LoginId=LoginId)
                login_serializer = LoginAuthSerializer(login)
                return JsonResponse(login_serializer.data, safe=False)
            else:
                return JsonResponse("", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("", safe=False)


@csrf_exempt
def CreateloginApi(request, pk=""):

    if request.method == 'POST':
        login_data = JSONParser().parse(request)
        login_serializer = LoginSaveSerializer(data=login_data)
        if login_serializer.is_valid():
            login_serializer.save()
            return JsonResponse("Add successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        loginData = JSONParser().parse(request)
        login = Login.objects.get(
            LoginId=loginData['LoginId'])
        logSerializer = LoginSaveSerializer(
            login, data=loginData)
        if logSerializer.is_valid():
            logSerializer.save()
            return JsonResponse("Update successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)


@csrf_exempt
def loginStatusApi(request, pk=""):

    if request.method == 'PUT':
        loginData = JSONParser().parse(request)
        login = Login.objects.get(
            UserId=loginData['UserId'],
            UserType=loginData['UserType'])
        logSerializer = LoginStatusSerializer(
            login, data=loginData)
        if logSerializer.is_valid():
            logSerializer.save()
            return JsonResponse("Update successfully", safe=False)
        return JsonResponse("", safe=False)


@csrf_exempt
def CheckEmailApi(request, pk=""):

    try:
        if request.method == 'POST':
            login_data = JSONParser().parse(request)
            login = Login.objects.filter(
                EmailId=login_data['EmailId'], UserType=login_data['UserType'],)
            login_serializer = LoginAuthSerializer(login, many=True)
            if login_serializer.data[0]:
                return JsonResponse("Email Id Already Registered", safe=False)
            else:
                return JsonResponse("", safe=False)
    except:
        return JsonResponse("", safe=False)


@csrf_exempt
def CheckEmailRestPasswordApi(request, pk=""):

    try:
        if request.method == 'POST':
            login_data = JSONParser().parse(request)
            login = Login.objects.filter(
                EmailId=login_data['EmailId'], UserType=login_data['UserType'],)
            login_serializer = LoginAuthSerializer(login, many=True)
            if login_serializer.data[0]:
                return JsonResponse(login_serializer.data, safe=False)
            else:
                return JsonResponse("", safe=False)
    except:
        return JsonResponse("", safe=False)


@csrf_exempt
def AdvertiserSocialLoginApi(request, pk=""):

    Data = []
    try:
        if request.method == 'POST':
            login_data = JSONParser().parse(request)
            loginDetail = []

            try:
                loginDetail = socialLogin(login_data)
            except:

                login_serializer = SocialLoginSerializer(data=login_data)
                if login_serializer.is_valid():
                    login_serializer.save()

                    Count = connection.cursor()
                    sql = "INSERT INTO `app_advertiser_profile`(`SortId`,`AdvertiserId`, `BusinessEmail`, `CompanyName`, `Credits`,`EnableMailUpdates`,`Status`,`IsUpgrade`,SMPicture) VALUES ('"+str(dt.now())+"','"+ login_data['UserId']+"','"+login_data['EmailId']+"','"+ login_data['CompanyName']+"','"+ login_data['Credits']+"','0','1','1','"+  login_data['SMPicture']+"')"
                    # return JsonResponse(sql, safe=False)
                    # val = (dt.now(), login_data['UserId'],
                    #        login_data['EmailId'], login_data['CompanyName'], int(login_data['Credits']), 0, 1, 1, login_data['SMPicture'])
                    Count.execute(sql)
                    profile = Profile.objects.get(
                        AdvertiserId=login_data['AdvertiserId'])
                    profileSerializer = SaveProfileSerializer(
                        profile, data=login_data)
                    if profileSerializer.is_valid():
                        profileSerializer.save()
                        loginDetail = socialLogin(login_data)

            UserToken_data = {}
            UserToken_data['EmailId'] = loginDetail['EmailId']
            UserToken_data['UserType'] = login_data['UserType']
            UserToken_data['LoginType'] = "Normal"
            UserToken_data['LoginId'] = loginDetail['LoginId']

            UserToken_serializer = UserTokenRegisterSerializer(
                data=UserToken_data)
            if UserToken_serializer.is_valid():
                UserToken_serializer.save()
            Data = []
            Data.append('SUCCESS')
            Data.append(loginDetail)  # logindata
            Data.append(UserToken_serializer.data['TokenId'])  # token
            userType = UserType.objects.get(
                UserTypeId=loginDetail['UserType'])
            userType_serializer = UserTypeSerializer(userType)
            if userType_serializer.data['UserType'] == 'Advertiser':
                profile = Profile.objects.get(
                    AdvertiserId=loginDetail['UserId'])
                profileSerializer = ProfileSerializer(
                    profile)
                Data.append(profileSerializer.data)  # UserData
            else:
                Data.append('')  # UserData
    except:
        Data.append('FAILED')
        Data.append('')  # logindata
        Data.append('')  # token
        Data.append('')  # UserData
    return JsonResponse(Data, safe=False)


@csrf_exempt
def PublisherSocialLoginApi(request, pk=""):

    if request.method == 'POST':
        login_data = JSONParser().parse(request)
        loginDetail = []
        try:
            loginDetail = socialLogin(login_data)
        except:

            login_serializer = SocialLoginSerializer(data=login_data)
            if login_serializer.is_valid():
                login_serializer.save()

                Count = connection.cursor()
                sql = "INSERT INTO `app_publisher_publisherregister`(`SortId`,`PublisherId`, `BusinessEmail`, `CompanyName`,`EnableBot`,`EnableMediaEntry`,`EnableMailUpdates`,`Status`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (dt.now(), login_data['PublisherId'],
                       login_data['EmailId'], login_data['CompanyName'], 0, 0, 0, 1)
                Count.execute(sql, val)
                loginDetail = socialLogin(login_data)


def socialLogin(login_data):
    login = Login.objects.get(
        UserId=login_data['UserId'], UserType=login_data['UserType'])
    staffRegisterSerializer = SocialLoginSerializer(
        login)
    return staffRegisterSerializer.data
    # return JsonResponse(staffRegisterSerializer.data, safe=False)


@csrf_exempt
def UserTokenApi(request, TokenId=""):
    if request.method == 'GET':
        Data = []
        if TokenId:
            UserToken_data = UserTokenRegister.objects.get(TokenId=TokenId)
            UserToken_serializer = UserTokenRegisterSerializer(
                UserToken_data)
        login_data = UserToken_serializer.data
        login_serializer = []
        login = Login.objects.filter(
            EmailId=login_data['EmailId'], LoginId=login_data['LoginId'], UserType=login_data['UserType'])
        Data = []
        login_serializer = LoginAuthSerializer(login, many=True)
        # return JsonResponse("login_serializer.data", safe=False)
        if not login_serializer.data:
            login = Login.objects.filter(
                EmailId=login_data['EmailId']).exclude(UserType=login_data['UserType'])
            login_serializer = LoginAuthSerializer(login, many=True)
            if not login_serializer.data:
                Data.append('FAILED')
                Data.append('')  # logindata
                Data.append('')  # token
                Data.append('')  # UserData
            else:
                Data.append('FAILED')
                Data.append(login_serializer.data[0])  # logindata
                Data.append('')  # token
                Data.append('')  # UserData
        else:
            Data.append('SUCCESS')
            Data.append(login_serializer.data[0])  # logindata
            Data.append(TokenId)  # token

            userType = UserType.objects.get(
                UserTypeId=login_serializer.data[0]['UserType'])
            userType_serializer = UserTypeSerializer(userType)
            if userType_serializer.data['UserType'] == 'Advertiser':
                profile = Profile.objects.get(
                    AdvertiserId=login_serializer.data[0]['UserId'])
                profileSerializer = ProfileSerializer(
                    profile)
                Data.append(profileSerializer.data)  # UserData
            else:
                Data.append('')  # UserData
        return JsonResponse(Data, safe=False)
    elif request.method == 'DELETE':
        try:
            UserToken_data = UserTokenRegister.objects.get(TokenId=TokenId)
            UserToken_data.delete()
            return JsonResponse("Deleted successfully", safe=False)
        except:
            return JsonResponse("Deleted successfully", safe=False)
