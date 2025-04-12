from email.message import EmailMessage
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from django.http.response import JsonResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from email.message import EmailMessage

from app_send_mail.views import sendGMKMail
from django.db import connection
# Create your views here.

@csrf_exempt
def RestCredits(request, pk=""):
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE `app_advertiser_profile` SET `Credits`= 0 WHERE DATE(`CreditsExpiryDate`) < DATE(NOW()) OR `CreditsExpiryDate` IS NULL")
        return JsonResponse("ok", safe=False)

    except:
        return JsonResponse("Invalid payload", safe=False)
