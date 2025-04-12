from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from app_user_plan.models import UserSitePlan, UserSitePlanItem
from app_user_plan.serializers import UserSitePlanItemSerializer, UserSitePlanSerializer

# Create your views here.


@csrf_exempt
def CURDSiteUserPlanApi(request, UserType="", pk=""):
    # try:
        if request.method == 'GET':
            if not pk:
                userSitePlan = UserSitePlan.objects.filter(UserTypeId=UserType)
                userSitePlanSerializer = UserSitePlanSerializer(
                    userSitePlan, many=True)
                return JsonResponse(userSitePlanSerializer.data, safe=False)
            else:
                userSitePlan = UserSitePlan.objects.get(
                    UserTypeId=UserType, SitePlanId=pk)
                userSitePlanSerializer = UserSitePlanSerializer(
                    userSitePlan)
                return JsonResponse(userSitePlanSerializer.data, safe=False)
        elif request.method == 'POST':
            userSitePlanData = JSONParser().parse(request)
            # return JsonResponse(userSitePlanData, safe=False)
            userSitePlanSerializer = UserSitePlanSerializer(
                data=userSitePlanData)
            if userSitePlanSerializer.is_valid():
                userSitePlanSerializer.save()
                return JsonResponse(userSitePlanSerializer.data['SitePlanId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            userSitePlanData = JSONParser().parse(request)
            userSitePlan = UserSitePlan.objects.get(
                SitePlanId=userSitePlanData['SitePlanId'])
            userSitePlanSerializer = UserSitePlanSerializer(
                userSitePlan, data=userSitePlanData)
            if userSitePlanSerializer.is_valid():
                userSitePlanSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            userSitePlan = UserSitePlan.objects.get(SitePlanId=pk)
            userSitePlan.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CURDSiteUserPlanItemApi(request,  pk=""):
    try:
        if request.method == 'GET':
            if not pk:
                userSitePlanItem = UserSitePlanItem.objects.all()
                userSitePlanItemSerializer = UserSitePlanItemSerializer(
                    userSitePlanItem, many=True)
                return JsonResponse(userSitePlanItemSerializer.data, safe=False)
            else:
                userSitePlanItem = UserSitePlanItem.objects.get( SitePlanItemId=pk)
                userSitePlanItemSerializer = UserSitePlanItemSerializer(
                    userSitePlanItem)
                return JsonResponse(userSitePlanItemSerializer.data, safe=False)
        elif request.method == 'POST':
            userSitePlanItemData = JSONParser().parse(request)
            # return JsonResponse(userSitePlanItemData, safe=False)
            userSitePlanItemSerializer = UserSitePlanItemSerializer(
                data=userSitePlanItemData)
            if userSitePlanItemSerializer.is_valid():
                userSitePlanItemSerializer.save()
                return JsonResponse(userSitePlanItemSerializer.data['SitePlanItemId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            userSitePlanItemData = JSONParser().parse(request)
            userSitePlanItem = UserSitePlanItem.objects.get(
                SitePlanItemId=userSitePlanItemData['SitePlanItemId'])
            userSitePlanItemSerializer = UserSitePlanItemSerializer(
                userSitePlanItem, data=userSitePlanItemData)
            if userSitePlanItemSerializer.is_valid():
                userSitePlanItemSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            userSitePlanItem = UserSitePlanItem.objects.get(
                SitePlanItemId=pk)
            userSitePlanItem.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)
