import json
from django.shortcuts import render
from io import BytesIO
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
# Create your views here.

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


data = {
    "company": "Dennnis Ivanov Company",
    "address": "123 Street name",
    "city": "Vancouver",
    "state": "WA",
    "zipcode": "98663",


    "phone": "555-555-2345",
    "email": "youremail@dennisivy.com",
    "website": "dennisivy.com",
}

# Opens up page as PDF


class ViewPDF(View):
    def get(self, request, *args, **kwargs):

        pdf = render_to_pdf('app/invoice.html')
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Estimate.pdf"
        content = "attachment; filename=%s" %(filename)
        response['Content-Disposition'] = content
        return response


# Automaticly downloads to PDF file
# class DownloadPDF(View):
#     def get(self, request, PlanId="", UserId="", *args, **kwargs):
#         try:
#             planDetail = CampaignPDFData.objects.get(
#                 UserId=UserId, CampaignId=PlanId)
#             campaignPDFDataSerializer = CampaignPDFDataSerializer(
#                 planDetail)
#             EstimateData = json.loads(campaignPDFDataSerializer.data['PDFData'])[0]
#             # return JsonResponse(EstimateData, safe=False)
#             # pdf = render_to_pdf('app/estimate.html', EstimateData)
#             # return HttpResponse(pdf, content_type='application/pdf')
#             pdf = render_to_pdf('app/estimate.html', EstimateData)

#             response = HttpResponse(pdf, content_type='application/pdf')
#             filename = "Estimate_%s.pdf" %(EstimateData['Campaign']['PlanName'])
#             content = "attachment; filename=%s" %(filename)
#             response['Content-Disposition'] = content
#             return response

#         except:
#             return JsonResponse("Invalid payload", safe=False)

def index(request):
    context = {}
    return render(request, 'app/index.html', context)

def getData(d):
	return "appu"