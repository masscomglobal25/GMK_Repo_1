import codecs
import hashlib
import os
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import smtplib
from email.message import EmailMessage
from random import randint
# Create your views here.


@csrf_exempt
def sendTestMail(self):

    msg = EmailMessage()
    # msg['Subject'] = 'Check out Bronx as a puppy!'
    msg['From'] = settings.EMAIL_HOST_USER
    msg['To'] = ['mintothomas009@gmail.com', 'rincejose888@gmail.com']

    # msg.set_content('This is a plain text email')

    # msg.add_alternative("""\
    # <!DOCTYPE html>
    # <html>
    #     <body>
    #         <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    #     </body>
    # </html>
    # """, subtype='html')

    msg = EmailMessage()
    msg['Subject'] = 'Verify your Account'
    msg['In-Reply-To'] = 'cs@globalmediakit.com'
    msg['From'] = settings.EMAIL_HOST_USER_NAME + \
        " <"+settings.EMAIL_HOST_USER+">"
    msg['To'] = ['mintothomas009@gmail.com', 'rincejose888@gmail.com']
    OTPCODE = str(random_with_N_digits(6))
    f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
        __file__)), "templates/app/advertiserVerifyAccount.html"), 'r')
    data = f.read()
    data = data.replace("{{code}}", OTPCODE)
    data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
    msg.set_content(data, subtype="plain", charset='us-ascii')
    msg.add_alternative(data, subtype='html')

    response = sendGMKMail(msg)
    return JsonResponse(response, safe=False)


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def sendGMKMail(msg=""):
    EMAIL_ADDRESS = settings.EMAIL_HOST_USER
    EMAIL_PASSWORD = settings.EMAIL_HOST_PASSWORD
    with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
        server.connect(settings.EMAIL_HOST, settings.EMAIL_PORT)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
    return "Success"


@csrf_exempt
def advertiserVerifyAccount(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            advertiserName = requestData['Name']
            advertiserMailId = requestData['EmailId']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'Verify your Account'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [advertiserName + " <"+advertiserMailId+">"]
            OTPCODE = str(random_with_N_digits(6))
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/advertiserRegistrationOTPVerification.html"), 'r')
            data = f.read()
            data = data.replace("{{code}}", OTPCODE)
            data = data.replace("{{advertiserName}}", advertiserName)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse(hashlib.sha1(OTPCODE.encode('utf-8')).hexdigest(), safe=False)
        elif request.method == 'PUT':
            requestData = JSONParser().parse(request)
            EncodedOTP = requestData['EncodedOTP']
            OTP = str(requestData['OTP'])
            UserCode = hashlib.sha1(OTP.encode('utf-8')).hexdigest()
            if UserCode == EncodedOTP:
                return JsonResponse("Success", safe=False)
            else:
                return JsonResponse("", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def advertiserResetPassword(request):

    # try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            advertiserName = requestData['Name']
            advertiserMailId = requestData['EmailId']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'Reset password'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [advertiserName + " <"+advertiserMailId+">"]
            OTPCODE = str(random_with_N_digits(6))
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/advertiserRestPassword.html"), 'r')
            data = f.read()
            data = data.replace("{{code}}", OTPCODE)
            data = data.replace("{{advertiserName}}", advertiserName)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse(hashlib.sha1(OTPCODE.encode('utf-8')).hexdigest(), safe=False)
        elif request.method == 'PUT':
            requestData = JSONParser().parse(request)
            EncodedOTP = requestData['EncodedOTP']
            OTP = str(requestData['OTP'])
            UserCode = hashlib.sha1(OTP.encode('utf-8')).hexdigest()
            if UserCode == EncodedOTP:
                return JsonResponse("Success", safe=False)
            else:
                return JsonResponse("", safe=False)
        else:
            return JsonResponse("", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def publisherVerifyAccount(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            publisherName = requestData['Name']
            publisherMailId = requestData['EmailId']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'Verify your Account'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [publisherName + " <"+publisherMailId+">"]
            OTPCODE = str(random_with_N_digits(6))
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/publisherRegistrationOTPVerification.html"), 'r')
            data = f.read()
            data = data.replace("{{code}}", OTPCODE)
            data = data.replace("{{publisherName}}", publisherName)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse(hashlib.sha1(OTPCODE.encode('utf-8')).hexdigest(), safe=False)
        elif request.method == 'PUT':
            requestData = JSONParser().parse(request)
            EncodedOTP = requestData['EncodedOTP']
            OTP = str(requestData['OTP'])
            UserCode = hashlib.sha1(OTP.encode('utf-8')).hexdigest()
            if UserCode == EncodedOTP:
                return JsonResponse("Success", safe=False)
            else:
                return JsonResponse("", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def publisherResetPassword(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            publisherName = requestData['Name']
            publisherMailId = requestData['EmailId']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'Reset password'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [publisherName + " <"+publisherMailId+">"]
            OTPCODE = str(random_with_N_digits(6))
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/publisherRestPassword.html"), 'r')
            data = f.read()
            data = data.replace("{{code}}", OTPCODE)
            data = data.replace("{{publisherName}}", publisherName)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse(hashlib.sha1(OTPCODE.encode('utf-8')).hexdigest(), safe=False)
        elif request.method == 'PUT':
            requestData = JSONParser().parse(request)
            EncodedOTP = requestData['EncodedOTP']
            OTP = str(requestData['OTP'])
            UserCode = hashlib.sha1(OTP.encode('utf-8')).hexdigest()
            if UserCode == EncodedOTP:
                return JsonResponse("Success", safe=False)
            else:
                return JsonResponse("", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def publisherSignUpSuccess(request):

    # try:
    if request.method == 'POST':
        requestData = JSONParser().parse(request)
        publisherName = requestData['MediaGroup']
        publisherMailId = requestData['EmailId']
        msg = EmailMessage()
        msg['In-Reply-To'] = 'cs@globalmediakit.com'
        msg['Subject'] = 'Let`s Empower your Media!'
        msg['From'] = settings.EMAIL_HOST_USER_NAME + \
            " <"+settings.EMAIL_HOST_USER+">"
        msg['To'] = [publisherName + " <"+publisherMailId+">"]
        f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
            __file__)), "templates/app/PublisherSignUpConfirmation.html"), 'r')
        data = f.read().replace("{{publisherName}}", publisherName)
        data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
        msg.set_content(data, subtype="plain", charset='us-ascii')
        msg.add_alternative(data, subtype='html')

        response = sendGMKMail(msg)
        # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
        return JsonResponse("ok", safe=False)
    else:
        return JsonResponse("", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def publisherSignUpSuccessToAdmin(request):

    # try:
    if request.method == 'POST':
        requestData = JSONParser().parse(request)
        MediaName = requestData['MediaName']
        MediaGroup = requestData['MediaGroup']
        BusinessMailId = requestData['EmailId']
        Country = requestData['Country']
        msg = EmailMessage()
        msg['In-Reply-To'] = 'cs@globalmediakit.com'
        msg['Subject'] = 'New Media Service Provider Sign Up'
        msg['From'] = settings.EMAIL_HOST_USER_NAME + \
            " <"+settings.EMAIL_HOST_USER+">"
        msg['To'] = ['Global Media KIt' + " <itservices@globalmediakit.com>"]
        f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
            __file__)), "templates/app/PublisherSignUpSuccessToAdmin.html"), 'r')
        data = f.read()
        data = data.replace("{{BusinessMailId}}", BusinessMailId)
        data = data.replace("{{MediaName}}", MediaName)
        data = data.replace("{{MediaGroup}}", MediaGroup)
        data = data.replace("{{Country}}", Country)
        data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
        msg.set_content(data, subtype="plain", charset='us-ascii')
        msg.add_alternative(data, subtype='html')

        response = sendGMKMail(msg)
        # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
        return JsonResponse("ok", safe=False)
    else:
        return JsonResponse("", safe=False)
    # except:
    #     return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def advertiserSignUpSuccess(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            advertiserName = requestData['Name']
            advertiserMailId = requestData['EmailId']
            CreditCount = requestData['CreditCount']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'Position your Brand!'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [advertiserName + " <"+advertiserMailId+">"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/advertiserSignUpConfirmation.html"), 'r')
            data = f.read()
            data = data.replace("{{CreditCount}}", CreditCount)
            data = data.replace("{{advertiserName}}", advertiserName)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse("ok", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def advertiserSignUpSuccessToAdmin(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            AdvertiserName = requestData['Name']
            BusinessMailId = requestData['EmailId']
            City = requestData['City']
            Country = requestData['Country']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'New Advertiser Sign Up'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = ['Global Media KIt' + " <itservices@globalmediakit.com>"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/advertiserSignUpSuccessToAdmin.html"), 'r')
            data = f.read()
            data = data.replace("{{BusinessMailId}}", BusinessMailId)
            data = data.replace("{{AdvertiserName}}", AdvertiserName)
            data = data.replace("{{City}}", City)
            data = data.replace("{{Country}}", Country)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse("ok", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def abandonedCart(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            advertiserName = requestData['Name']
            advertiserMailId = requestData['EmailId']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'You have left something in your cart'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [advertiserName + " <"+advertiserMailId+">"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/abandonedCart.html"), 'r')
            data = f.read()
            data = data.replace("{{CreditCount}}", "100")
            data = data.replace("{{advertiserName}}", advertiserName)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse("ok", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def planCreatedByAdvertiser(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            AdvertiserName = requestData['AdvertiserName']
            advertiserMailId = requestData['EmailId']
            PlanName = requestData['PlanName']
            PlanLink = requestData['PlanLink']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'Your Media Plan has been Created!'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [AdvertiserName + " <"+advertiserMailId+">"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/planCreatedByAdvertiser.html"), 'r')
            data = f.read()
            data = data.replace("{{PlanName}}", PlanName)
            data = data.replace("{{AdvertiserName}}", AdvertiserName)
            data = data.replace("{{PlanLink}}", PlanLink)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse("ok", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def planCreatedWithPremiumSupportByAdvertiser(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            AdvertiserName = requestData['AdvertiserName']
            advertiserMailId = requestData['EmailId']
            PlanName = requestData['PlanName']
            PlanLink = requestData['PlanLink']
            PremiumExpertAssistanceNote = requestData['PremiumExpertAssistanceNote']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'Premium Expert Assistance Request Confirmation'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [AdvertiserName + " <"+advertiserMailId+">"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/planCreatedWithPremiumSupportByAdvertiser.html"), 'r')
            data = f.read()
            data = data.replace("{{PlanName}}", PlanName)
            data = data.replace("{{AdvertiserName}}", AdvertiserName)
            data = data.replace("{{PlanLink}}", PlanLink)
            data = data.replace(
                "{{PremiumExpertAssistanceNote}}", PremiumExpertAssistanceNote)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse("ok", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def planCreatedWithPremiumSupportByAdvertiserToAdmin(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            AdvertiserName = requestData['AdvertiserName']
            advertiserMailId = requestData['EmailId']
            PlanName = requestData['PlanName']
            PlanLink = requestData['PlanLink']
            PremiumExpertAssistanceNote = requestData['PremiumExpertAssistanceNote']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = AdvertiserName + \
                ' has opted for Premium Expert Assistance'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = ['Global Media KIt' + " <itservices@globalmediakit.com>"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/planCreatedWithPremiumSupportByAdvertiserToAdmin.html"), 'r')
            data = f.read()
            data = data.replace("{{PlanName}}", PlanName)
            data = data.replace("{{AdvertiserName}}", AdvertiserName)
            data = data.replace("{{PlanLink}}", PlanLink)
            data = data.replace(
                "{{PremiumExpertAssistanceNote}}", PremiumExpertAssistanceNote)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse("ok", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def twoDaysAfterPlanCreate(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            AdvertiserName = requestData['AdvertiserName']
            advertiserMailId = requestData['EmailId']
            PlanName = requestData['PlanName']
            PlanLink = requestData['PlanLink']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'Attention - Your Media Plan is Expiring soon'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [AdvertiserName + " <"+advertiserMailId+">"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/twoDaysAfterPlanCreate.html"), 'r')
            data = f.read()
            data = data.replace("{{PlanName}}", PlanName)
            data = data.replace("{{AdvertiserName}}", AdvertiserName)
            data = data.replace("{{PlanLink}}", PlanLink)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse("ok", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def sevenDaysAfterPlanCreate(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            AdvertiserName = requestData['AdvertiserName']
            advertiserMailId = requestData['EmailId']
            PlanName = requestData['PlanName']
            PlanLink = requestData['PlanLink']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'Media Plan <name> Submitted for Approval'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [AdvertiserName + " <"+advertiserMailId+">"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/sevenDaysAfterPlanCreate.html"), 'r')
            data = f.read()
            data = data.replace("{{PlanName}}", PlanName)
            data = data.replace("{{AdvertiserName}}", AdvertiserName)
            data = data.replace("{{PlanLink}}", PlanLink)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse("ok", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def planSendForApprovalForAdvertiser(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            AdvertiserName = requestData['AdvertiserName']
            advertiserMailId = requestData['EmailId']
            PlanName = requestData['PlanName']
            PlanLink = requestData['PlanLink']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'Media Plan '+PlanName+' Submitted for Approval'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [AdvertiserName + " <"+advertiserMailId+">"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/planSendForApprovalForAdvertiser.html"), 'r')
            data = f.read()
            data = data.replace("{{PlanName}}", PlanName)
            data = data.replace("{{AdvertiserName}}", AdvertiserName)
            data = data.replace("{{PlanLink}}", PlanLink)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse(response, safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def planSendForApprovalForPublisher(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            PublisherName = requestData['PublisherName']
            MailId = requestData['EmailId']
            PlanName = requestData['PlanName']
            # MediaSelected = requestData['MediaSelected']
            StartDate = requestData['StartDate']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'You`ve got a new media plan for review'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [PublisherName + " <"+MailId+">"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/planSendForApprovalForPublisher.html"), 'r')
            data = f.read()
            data = data.replace("{{PlanName}}", PlanName)
            data = data.replace("{{PublisherName}}", PublisherName)
            # data = data.replace("{{MediaSelected}}", MediaSelected)
            data = data.replace("{{StartDate}}", StartDate)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse("ok", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def twoDaysAfterPlanSendForApprovalForPublisher(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            PublisherName = requestData['PublisherName']
            MailId = requestData['EmailId']
            PlanName = requestData['PlanName']
            PlanLink = requestData['PlanLink']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'Media Plan '+PlanName+'  is Awaiting Review'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [PublisherName + " <"+MailId+">"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/twoDaysAfterPlanSendForApprovalForPublisher.html"), 'r')
            data = f.read()
            data = data.replace("{{PlanName}}", PlanName)
            data = data.replace("{{PublisherName}}", PublisherName)
            data = data.replace("{{PlanLink}}", PlanLink)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse("ok", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def planSendForApprovalForAdmin(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            AdvertiserName = requestData['AdvertiserName']
            PlanName = requestData['PlanName']
            PlanLink = requestData['PlanLink']
            MediaName = requestData['MediaName']
            StartDate = requestData['StartDate']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'Media Plan '+PlanName+' Sent for Approval'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = ['Global Media KIt' + " <itservices@globalmediakit.com>"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/planSendForApprovalForAdmin.html"), 'r')
            data = f.read()
            data = data.replace("{{PlanName}}", PlanName)
            data = data.replace("{{AdvertiserName}}", AdvertiserName)
            data = data.replace("{{MediaName}}", MediaName)
            data = data.replace("{{StartDate}}", StartDate)
            data = data.replace("{{PlanLink}}", PlanLink)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse("ok", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def planApprovedByPublisherForAdvertiser(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            AdvertiserName = requestData['AdvertiserName']
            advertiserMailId = requestData['EmailId']
            PlanName = requestData['PlanName']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'Your Media plan have been Updated'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [AdvertiserName + " <"+advertiserMailId+">"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/planApprovedByPublisherForAdvertiser.html"), 'r')
            data = f.read()
            data = data.replace("{{PlanName}}", PlanName)
            data = data.replace("{{AdvertiserName}}", AdvertiserName)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse(response, safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def PlanBookingConfirmedByAdvertiserToAdvertiser(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            AdvertiserName = requestData['AdvertiserName']
            advertiserMailId = requestData['EmailId']
            PlanName = requestData['PlanName']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'Your Media plan have been Updated'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [AdvertiserName + " <"+advertiserMailId+">"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/PlanBookingConfirmedByAdvertiserToAdvertiser.html"), 'r')
            data = f.read()
            data = data.replace("{{PlanName}}", PlanName)
            data = data.replace("{{AdvertiserName}}", AdvertiserName)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse(response, safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def PlanBookingConfirmedByAdvertiserToAdmin(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            AdvertiserName = requestData['AdvertiserName']
            PlanName = requestData['PlanName']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = AdvertiserName+' has approved the '+PlanName
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = ['Global Media KIt' + " <itservices@globalmediakit.com>"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/PlanBookingConfirmedByAdvertiserToAdmin.html"), 'r')
            data = f.read()
            data = data.replace("{{PlanName}}", PlanName)
            data = data.replace("{{AdvertiserName}}", AdvertiserName)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse(response, safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def PlanBookingCancelledByAdvertiserToAdmin(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            AdvertiserName = requestData['AdvertiserName']
            PlanName = requestData['PlanName']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = AdvertiserName + \
                ' cancelled the Media Plan '+PlanName
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = ['Global Media KIt' + " <itservices@globalmediakit.com>"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/PlanBookingCancelledByAdvertiserToAdmin.html"), 'r')
            data = f.read()
            data = data.replace("{{PlanName}}", PlanName)
            data = data.replace("{{AdvertiserName}}", AdvertiserName)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse(response, safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)

@csrf_exempt
def PlanBookingConfirmedByAdvertiserForPublisher(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            PublisherName = requestData['PublisherName']
            MailId = requestData['EmailId']
            PlanName = requestData['PlanName']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'Media Plan Approved by Advertiser'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [PublisherName + " <"+MailId+">"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/PlanBookingConfirmedByAdvertiserForPublisher.html"), 'r')
            data = f.read()
            data = data.replace("{{PlanName}}", PlanName)
            data = data.replace("{{PublisherName}}", PublisherName)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse("ok", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def PlanBookingCancelledByAdvertiserToAdvertiser(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            AdvertiserName = requestData['AdvertiserName']
            advertiserMailId = requestData['EmailId']
            PlanName = requestData['PlanName']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'You have cancelled the Media Plan '+PlanName
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [AdvertiserName + " <"+advertiserMailId+">"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/PlanBookingCancelledByAdvertiserToAdvertiser.html"), 'r')
            data = f.read()
            data = data.replace("{{PlanName}}", PlanName)
            data = data.replace("{{AdvertiserName}}", AdvertiserName)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse(response, safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def PlanBookedSucessfullyToAdvertiser(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            AdvertiserName = requestData['AdvertiserName']
            advertiserMailId = requestData['EmailId']
            PlanName = requestData['PlanName']
            OpportunityName = requestData['OpportunityName']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = PlanName+'Campaign Successfully Booked'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [AdvertiserName + " <"+advertiserMailId+">"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/PlanBookedSucessfullyToAdvertiser.html"), 'r')
            data = f.read()
            data = data.replace("{{OpportunityName}}", OpportunityName)
            data = data.replace("{{AdvertiserName}}", AdvertiserName)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse(response, safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def MediaApprovalSubmittedForPublisher(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            PublisherName = requestData['PublisherName']
            MailId = requestData['EmailId']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'Your listing is under review'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [PublisherName + " <"+MailId+">"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/MediaApprovalSubmittedForPublisher.html"), 'r')
            data = f.read()
            data = data.replace("{{PublisherName}}", PublisherName)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse("ok", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def MediaRejectedByAdminForPublisher(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            PublisherName = requestData['PublisherName']
            MailId = requestData['EmailId']
            MediaName = requestData['MediaName']
            OpportunityName = requestData['OpportunityName']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'Your listing is rejected'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [PublisherName + " <"+MailId+">"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/MediaRejectedByAdminForPublisher.html"), 'r')
            data = f.read()
            data = data.replace("{{MediaName}}", MediaName)
            data = data.replace("{{OpportunityName}}", OpportunityName)
            data = data.replace("{{PublisherName}}", PublisherName)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse("ok", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def MediaApprovedByAdminForPublisher(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            PublisherName = requestData['PublisherName']
            MediaViewLink = requestData['MediaViewLink']
            MailId = requestData['EmailId']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'Your Listing is approved'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [PublisherName + " <"+MailId+">"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/MediaApprovedByAdminForPublisher.html"), 'r')
            data = f.read()
            data = data.replace("{{MediaViewLink}}", MediaViewLink)
            data = data.replace("{{PublisherName}}", PublisherName)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse("ok", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def MediaActivatesByAdminForPublisher(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            MediaName = requestData['MediaName']
            OpportunityName = requestData['OpportunityName']
            PublisherName = requestData['PublisherName']
            MailId = requestData['EmailId']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'Your Listing is Activated'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [PublisherName + " <"+MailId+">"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/MediaActivatesByAdminForPublisher.html"), 'r')
            data = f.read()
            data = data.replace("{{MediaName}}", MediaName)
            data = data.replace("{{OpportunityName}}", OpportunityName)
            data = data.replace("{{PublisherName}}", PublisherName)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse("ok", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def MediaApprovalSubmittedForAdmin(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            PublisherName = requestData['PublisherName']
            MediaName = requestData['MediaName']
            MediaType = requestData['MediaType']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = PublisherName + \
                ' has submitted a listing for approval'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = ['Global Media KIt' + " <itservices@globalmediakit.com>"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/MediaApprovalSubmittedForAdmin.html"), 'r')
            data = f.read()
            data = data.replace("{{MediaType}}", MediaType)
            data = data.replace("{{PublisherName}}", PublisherName)
            data = data.replace("{{MediaName}}", MediaName)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse(response, safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def MediaAdUintApprovalSubmittedForPublisher(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            PublisherName = requestData['PublisherName']
            MediaName = requestData['MediaName']
            MailId = requestData['EmailId']
            MediaType = requestData['MediaType']
            OpportunityName = requestData['OpportunityName']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'You`ve got a new media plan for review'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [PublisherName + " <"+MailId+">"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/MediaAdUintApprovalSubmittedForPublisher.html"), 'r')
            data = f.read()
            data = data.replace("{{MediaType}}", MediaType)
            data = data.replace("{{MediaName}}", MediaName)
            data = data.replace("{{OpportunityName}}", OpportunityName)
            data = data.replace("{{PublisherName}}", PublisherName)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse("ok", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def MediaAdUintApprovalSubmittedForAdmin(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            PublisherName = requestData['PublisherName']
            MediaName = requestData['MediaName']
            MediaType = requestData['MediaType']
            OpportunityName = requestData['OpportunityName']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = PublisherName + \
                ' has submitted a listing for approval'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = ['Global Media KIt' + " <itservices@globalmediakit.com>"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/MediaAdUintApprovalSubmittedForAdmin.html"), 'r')
            data = f.read()
            data = data.replace("{{MediaType}}", MediaType)
            data = data.replace("{{PublisherName}}", PublisherName)
            data = data.replace("{{OpportunityName}}", OpportunityName)
            data = data.replace("{{MediaName}}", MediaName)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse(response, safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def MeetingRequestByAdvertiserForAdmin(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            AdvertiserName = requestData['AdvertiserName']
            HelpRequest = requestData['HelpRequest']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'New callback request'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = ['Global Media KIt' + " <itservices@globalmediakit.com>"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/MeetingRequestByAdvertiserForAdmin.html"), 'r')
            data = f.read()
            data = data.replace("{{AdvertiserName}}", AdvertiserName)
            data = data.replace("{{HelpRequest}}", HelpRequest)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse(response, safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def MeetingRequestByAdvertiserForAdvertiser(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            AdvertiserName = requestData['AdvertiserName']
            advertiserMailId = requestData['EmailId']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'Thank you for your callback request!'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [AdvertiserName + " <"+advertiserMailId+">"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/MeetingRequestByAdvertiserForAdvertiser.html"), 'r')
            data = f.read()
            data = data.replace("{{AdvertiserName}}", AdvertiserName)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse(response, safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def MeetingRequestByPublisherForAdmin(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            PublisherName = requestData['PublisherName']
            HelpRequest = requestData['HelpRequest']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'New callback request'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = ['Global Media KIt' + " <itservices@globalmediakit.com>"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/MeetingRequestByPublisherForAdmin.html"), 'r')
            data = f.read()
            data = data.replace("{{PublisherName}}", PublisherName)
            data = data.replace("{{HelpRequest}}", HelpRequest)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse(response, safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def MeetingRequestByPublisherForPublisher(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            PublisherName = requestData['PublisherName']
            MailId = requestData['EmailId']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'Thank you for your callback request!'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [PublisherName + " <"+MailId+">"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/MeetingRequestByPublisherForPublisher.html"), 'r')
            data = f.read()
            data = data.replace("{{PublisherName}}", PublisherName)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse("ok", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CreditRequestByAdvertiserForAdmin(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            AdvertiserName = requestData['AdvertiserName']
            CreditNumber = requestData['CreditNumber']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'New Ad Credit request'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = ['Global Media KIt' + " <itservices@globalmediakit.com>"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/CreditRequestByAdvertiserForAdmin.html"), 'r')
            data = f.read()
            data = data.replace("{{AdvertiserName}}", AdvertiserName)
            data = data.replace("{{CreditNumber}}", CreditNumber)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse(response, safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)


@csrf_exempt
def CreditRequestByAdvertiserForAdvertiser(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            AdvertiserName = requestData['AdvertiserName']
            CreditNumber = requestData['CreditNumber']
            MailId = requestData['EmailId']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'Your Ad Credits request has been received'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [AdvertiserName + " <"+MailId+">"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/CreditRequestByAdvertiserForAdvertiser.html"), 'r')
            data = f.read()
            data = data.replace("{{AdvertiserName}}", AdvertiserName)
            data = data.replace("{{CreditNumber}}", CreditNumber)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse("ok", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)

@csrf_exempt
def CreditRequestProceedByAdminForAdvertiser(request):

    try:
        if request.method == 'POST':
            requestData = JSONParser().parse(request)
            AdvertiserName = requestData['AdvertiserName']
            CreditNumber = requestData['CreditNumber']
            MailId = requestData['EmailId']
            msg = EmailMessage()
            msg['In-Reply-To'] = 'cs@globalmediakit.com'
            msg['Subject'] = 'Your Ad Credits has been credited.'
            msg['From'] = settings.EMAIL_HOST_USER_NAME + \
                " <"+settings.EMAIL_HOST_USER+">"
            msg['To'] = [AdvertiserName + " <"+MailId+">"]
            f = codecs.open(os.path.join(os.path.dirname(os.path.dirname(
                __file__)), "templates/app/CreditRequestProceedByAdminForAdvertiser.html"), 'r')
            data = f.read()
            data = data.replace("{{AdvertiserName}}", AdvertiserName)
            data = data.replace("{{CreditNumber}}", CreditNumber)
            data = data.replace("{{BestRegrads}}", settings.GMK_MAIL_REGRADS)
            msg.set_content(data, subtype="plain", charset='us-ascii')
            msg.add_alternative(data, subtype='html')

            response = sendGMKMail(msg)
            # hashlib.sha1(repr(OTPCODE).encode('utf-8')).hexdigest()
            return JsonResponse("ok", safe=False)
        else:
            return JsonResponse("", safe=False)
    except:
        return JsonResponse("Invalid payload", safe=False)
