from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from app_site_user_request.models import SiteRequest

from app_site_user_request.serializers import SiteRequestSerializer


@csrf_exempt
def CURDSiteRequestApi(request, UserType="", pk=""):
    # try:
        if request.method == 'GET':
            if not pk:
                siteRequest = SiteRequest.objects.filter(UserTypeId=UserType)
                siteRequestSerializer = SiteRequestSerializer(
                    siteRequest, many=True)
                return JsonResponse(siteRequestSerializer.data, safe=False)
            else:
                siteRequest = SiteRequest.objects.get(
                    UserTypeId=UserType, SiteRequestId=pk)
                siteRequestSerializer = SiteRequestSerializer(
                    siteRequest)
                return JsonResponse(siteRequestSerializer.data, safe=False)
        elif request.method == 'POST':
            siteRequestData = JSONParser().parse(request)
            # return JsonResponse(siteRequestData, safe=False)
            siteRequestSerializer = SiteRequestSerializer(
                data=siteRequestData)
            if siteRequestSerializer.is_valid():
                siteRequestSerializer.save()
                return JsonResponse(siteRequestSerializer.data['SiteRequestId'], safe=False)
            return JsonResponse("Failed to add", safe=False)
        elif request.method == 'PUT':
            siteRequestData = JSONParser().parse(request)
            siteRequest = SiteRequest.objects.get(
                SiteRequestId=siteRequestData['SiteRequestId'])
            siteRequestSerializer = SiteRequestSerializer(
                siteRequest, data=siteRequestData)
            if siteRequestSerializer.is_valid():
                siteRequestSerializer.save()
                return JsonResponse("Update successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        elif request.method == 'DELETE':
            siteRequest = SiteRequest.objects.get(SiteRequestId=pk)
            siteRequest.delete()
            return JsonResponse("Deleted successfully", safe=False)
        else:
            return JsonResponse("Invalid request", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)
