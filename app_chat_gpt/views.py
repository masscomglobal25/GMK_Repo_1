from bs4 import BeautifulSoup
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import os

import openai

import re

from app_publisher.models import PublisherRegister
from app_publisher.serializers import PublisherSerializer
from app_vertical_media.models import MediaAdTypeImage
from app_vertical_media.serializers import UploadMediaAdTypeImageSerializer


openai.api_key = os.environ.get('OPENAI_API_KEY')


def generate_response(prompt):
    prompt = f"{prompt}"
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=3000,
        n=2,
        stop=None,
        temperature=0.5,
    )
    # Extract the generated response from the API result
    generated_text = response.choices[0].text.strip()
    # Remove any trailing text after the final sentence
    generated_text = re.sub(r"\n.*", "", generated_text)
    # Return the generated response
    return response


@csrf_exempt
def ConvertContentWithPrompt(request):
    data = JSONParser().parse(request)
    try:
        if request.method == 'POST':
            response = generate_response(data['Prompt'])
            response.choices[0].text = response.choices[0].text.replace(
                '\n\n\n\n', '<br/>')
            response.choices[0].text = response.choices[0].text.replace(
                '\n\n\n', '<br/>')
            response.choices[0].text = response.choices[0].text.replace(
                '\n\n', '<br/>')
            response.choices[0].text = response.choices[0].text.replace(
                '\n', '<br/>')
            return JsonResponse(response.choices[0].text, safe=False)
    except:
        return JsonResponse(data['ActualContent'], safe=False)
    # except openai.error.OpenAIError as e:
    #     return JsonResponse(f"OpenAI API error: {e}", safe=False)
    #     return None
    # except Exception as e:
    #     return JsonResponse(f"An error occurred: {e}", safe=False)
    #     return None


@csrf_exempt
def TestConvertContentWithPrompt(request):
    data = "Create a media recommendation as told by a media planning expert for Radio advertising without mentioning the Radio,  targeting Arts & Cinema category audience  for their  Brand Launch campaign, recommending them to add the following advertising opportunity to their media plan and proceed to submit this option for review. Assure them that as you proceed with the plan , our team of experts will support them launch the campaign and to get the best value for it .Use some bullet points in between ,use maximum 400 words and do not address this to anyone. Also use words Now, New, You in plenty  - THE BIG BREAKFAST CLUB - Four weeks show Sponsorship You can effectively promote your brand and connect with the Malayali community in the UAE through for weeks sponsorship of Hit 967 FM's popular morning show, The Big Breakfast Club. This show has a wide listenership and offers an excellent opportunity to reach out to potential customers during peak listening hours.a) 4 TOP of the Hour credit per day (brand  name only) - This means your brand name will be mentioned during every  Top of the Hour Promo ( 6 am, 7 am, 8 am, 9 am and 10 am ) which will  be a programme title mention.b) As a part of the sponsorship, you will get free Radio spots You will  get Two 30 sec spots inside the show ( This is a total of 40 spots in  total for four weeks, calculated based on Three spots on weekdays  (Mon-Fri) every day during THE BIG BREAKFAST CLUB (06 AM   11 AM) for  20 days )c) 4 Show Sweepers per day (+  10-word Tagline)outside the show ( This is a total of 80 show sweepers in  total for four weeks, calculated based on 4 show sweepers on weekdays  (Mon-Fri) every day, during other shows outside the Big Breakfast  Show for 20 days. Show sweepers are programme promos to drive more  listenership for the show. During these sweepers, your brand mention will  be told as a sponsor along with other sponsors )d) 4  Promos per day (brand name only) - (  This is a total of 80 show promos in total for four weeks, calculated  based on 4 promos for your brand on weekdays (Mon-Fri) every day, during  other shows outside the Big Breakfast Show The  difference between promos and Show sweepers is that in Promos, only  your brand's name will be told as the programme sponsor of the Big Breakfast  Show.e) Live Brand Mention of 15 sec  1 per week (Total 4 for four weeks)Here your brand and advertising message will be mentioned as a 15-second promo spot by the RJ once every week. f) Your brand Logo on the Sponsorship page on Hit FM website on THE BIG BREAKFAST CLUB show page g) Online Mpu / Leader Board of your brand will be placed on Hit FM webpages for a period of one week. h) One spot production with  one male or Female radio spot recording professional Artist comes free  with this package. The spot script should be finalized before the  recording is done for this. Our team will send you voice samples and  will assist you with recommendations and support to get an impactful  radio commercial which will align with your ad campaign requirements."
    # response = generate_response('Create a media recommendation in a problem solution format without mentioning problem and solution in headings in less than 300 words as an expert global media planner,targeting marketers who are planning a new campaign targeting sports category audience for their seasonal push/offers ,encouraging them to add the following advertising opportunity to their media plan.Use some bullet points in between and at last give three copy suggestions with "Stay healthy this Ramadan" for Out of Home advertising for brand name Sony  -Target visitors across Sheikh Mohammed bin Rashid Boulevard and traffic from and to Al Khail and SZR. Close proximity to The Address Downtown, Souk Al Bahar, Premium Hotels & Residential Buildings, entrance to TDM Cinema Carpark The largest DOOH across downtown, and MBR Boulevard')
    response = generate_response(data)
    return JsonResponse(response, safe=False)


@csrf_exempt
def GenerateAiPlan(request):


    request_data = JSONParser().parse(request)
    verticalSQL = ""
    if request_data['Vertical']:
        sql_data = ""
        for index, vertical in enumerate(request_data['Vertical']):
            if index > 0:
                sql_data = sql_data + " , "
            sql_data = sql_data + "'" + vertical + "'"
        if sql_data:
            verticalSQL = " AND app_vertical_media_media.VerticalType IN (" + \
                sql_data+")"

    languageSQL = ""
    if request_data['Language']:
        languageSQL = " AND ( "
        for index, language in enumerate(request_data['Language']):
            if index > 0:
                languageSQL = languageSQL + "  OR "
            languageSQL = languageSQL + "  app_vertical_media_media.PrimaryLanguage='"+language + \
                "' OR JSON_CONTAINS(`app_vertical_media_media`.`Language`,'" + \
                '"'+language+'"'+"')=1 "
        languageSQL = languageSQL+" ) "

    countrySQL = ""
    if request_data['Country']:
        countrySQL = " AND `app_vertical_media_media`.`CountryEvent` LIKE '%%" + \
            request_data['Country']+"%%' "

    cityRegionSQL = ""
    if request_data['City']:
        cityRegionSQL = " AND ( "
        for index, city in enumerate(request_data['City']):
            if index > 0:
                cityRegionSQL = cityRegionSQL + "  OR "
            cityRegionSQL = cityRegionSQL + \
                " JSON_CONTAINS(`app_vertical_media_media`.`CityRegion`,'" + \
                '"'+city+'"'+"')=1 "
        cityRegionSQL = cityRegionSQL + " ) "

    matchingCategorySQL = ""
    if request_data['MatchingCategoryId']:
        matchingCategorySQL = " AND ( "
        for index, matchingCategory in enumerate(request_data['MatchingCategoryId']):
            if index > 0:
                matchingCategorySQL = matchingCategorySQL + "  OR "
            matchingCategorySQL = matchingCategorySQL + \
                " JSON_CONTAINS(app_vertical_media_mediaadtype.MatchingCategories,'" + \
                '"'+matchingCategory+'"'+"')=1"
        matchingCategorySQL = matchingCategorySQL + " ) "
    incomeGroupSQL = ""
    if request_data['IncomeGroupId']:
        incomeGroupSQL = " AND ( "
        for index, incomeGroup in enumerate(request_data['IncomeGroupId']):
            if index > 0:
                incomeGroupSQL = incomeGroupSQL + "  OR "
            incomeGroupSQL = incomeGroupSQL + \
                " JSON_CONTAINS(app_vertical_media_mediaadtype.IncomeGroup,'" + \
                '"'+incomeGroup+'"'+"')=1  "
        incomeGroupSQL = incomeGroupSQL + " ) "

    sql = "SELECT media.*, (app_admin_estimatedreach.ReachFrom +  IF(app_admin_estimatedreach.ReachTo>0, app_admin_estimatedreach.ReachTo,  " + \
        "  app_admin_estimatedreach.ReachFrom))/2 as AdUnitAverageReach  FROM  " + \
        " (SELECT app_vertical_media_mediaadtype.*,app_vertical_media_media.`MediaId` as AdUnitMediaId,app_vertical_media_media.`VerticalType`,  " + \
        " app_vertical_media_media.`MediaName`,app_vertical_media_media.`Category`,  " + \
        " app_vertical_media_media.`PrimaryLanguage`,app_vertical_media_media.`TimeZone`,app_vertical_media_media.`MediaManagedBy`,  " + \
        " app_vertical_media_media.`WebsiteLink`,app_vertical_media_media.`EventVenue`,  " + \
        " app_vertical_media_media.`PublisherId`,app_vertical_media_media.`CountryEvent`,app_vertical_media_media.`CityRegion`,  " + \
        " app_vertical_media_media.`Language`,app_vertical_media_media.`EstimateReached`,  " + \
        " app_vertical_media_media.`BenefitsOfAdvertising`,app_vertical_media_media.`PromoVideoLink` as MediaPromoVideoLink ,  " + \
        " app_vertical_media_media.`MediaKit`,app_vertical_media_media.`MapLink`,  " + \
        " app_vertical_media_media.`Latitude`,app_vertical_media_media.`Longitude`,app_vertical_media_media.`IsHyperlocal`,  " + \
        " app_vertical_media_media.`Availability` as MediaAvailability ,app_vertical_media_media.`MediaImage`,  " + \
        " app_vertical_media_media.`ViewsCount`,app_vertical_media_media.`ModifiedDate`,app_vertical_media_media.`WebStatsOnOff`,  " + \
        " app_vertical_media_media.`RecommendedMedia`,app_vertical_media_media.`MediaCategory`,  " + \
        " app_vertical_media_media.`ViewOnlyMediaStore`,app_vertical_media_media.`ContactPerson`,  " + \
        " app_vertical_media_media.`Identification` as MediaIdentification,app_vertical_media_media.`SEOMetaDescription`,  " + \
        " app_vertical_media_media.`SEOMetaKeyword`,app_vertical_media_media.`SEOMetaTitle` , " + \
        " (SELECT `OrderNo` FROM `app_default_adunitcategory` WHERE `AdUnitCategoryId`=app_vertical_media_mediaadtype.AdUnitCategory) as AdUnitCategoryOrder , " + \
        " (SELECT `AdUnitCategory` FROM `app_default_adunitcategory` WHERE `AdUnitCategoryId`=app_vertical_media_mediaadtype.AdUnitCategory) as AdUnitCategoryName  " + \
        " FROM  " + \
        "`app_vertical_media_media` JOIN `app_vertical_media_mediaadtype` ON  " + \
        " app_vertical_media_mediaadtype.AdUnitCategory IS NOT NULL AND app_vertical_media_mediaadtype.AdUnitCategory <>'' AND  " + \
        " app_vertical_media_mediaadtype.ShowOnOff=1 AND  " + \
        " app_vertical_media_mediaadtype.Status IN (2,1)  and  " + \
        " app_vertical_media_media.ShowOnOff=1 AND  " + \
        " app_vertical_media_media.Status IN (2,1) AND  " + \
        " app_vertical_media_media.MediaId=app_vertical_media_mediaadtype.MediaId " + \
        verticalSQL + \
        languageSQL + \
        countrySQL + \
        cityRegionSQL + \
        matchingCategorySQL + \
        incomeGroupSQL + \
        " ) as media JOIN app_admin_estimatedreach on app_admin_estimatedreach.EstimatedReachId=media.AdTypeEstimateReached    " + \
        " ORDER BY AdUnitCategoryOrder,AdUnitAverageReach DESC   LIMIT 15 OFFSET " + \
        str(request_data['PageCount'])

    # return JsonResponse(request_data['Language'], safe=False)
    mediaDataForPrompt = []
    mediaDataAll = []
    mediaAdType = connection.cursor()
    mediaAdType.execute(sql)
    field_names = [i[0] for i in mediaAdType.description]

    for media in mediaAdType.fetchall():
        j = 0
        MediaAdUnit = {}
        adunitData = {}
        for col in media:
            if j < len(field_names):
                MediaAdUnit[str(field_names[j])] = col
                j = j + 1

        adunitData['id'] = MediaAdUnit['Identification']
        # adunitData['Description'] = remove_html_tags(
        #     MediaAdUnit['MediaAdUnitDescription']).replace(','," ")
        adunitname = ""
        if (MediaAdUnit['MediaAdType'] == "Package"):
            adunitname = MediaAdUnit['PackageName'].replace(
                ',', " ").replace('"', "'")
        elif (MediaAdUnit['MediaAdType'] == "Ad Unit"):
            adunitname = MediaAdUnit['SiteName'].replace(
                ',', " ").replace('"', "'")
        adunitData['MediaName'] = adunitname + " - " + \
            MediaAdUnit['MediaName'].replace(',', " ").replace('"', "'")
        MediaAdUnit['ImageName'] = ""
        mediaAdType = MediaAdTypeImage.objects.filter(
            MediaAdTypeId=MediaAdUnit['MediaAdTypeId'])
        mediaAdTypeSerializer = UploadMediaAdTypeImageSerializer(
            mediaAdType)
        MediaAdUnit['ImageName']=mediaAdTypeSerializer.data
        MediaAdUnit['PublisherDetails'] = ""
        if MediaAdUnit['PublisherId']:
            profile = PublisherRegister.objects.get(
                PublisherId=MediaAdUnit['PublisherId'])
            profileSerializer = PublisherSerializer(
                profile)
            MediaAdUnit['PublisherDetails'] = profileSerializer.data
        mediaDataForPrompt.append(adunitData)
        mediaDataAll.append(MediaAdUnit)
    BrandName = ""
    if request_data['BrandName']:
        BrandName = request_data['BrandName'].replace(
            ',', " ").replace('"', "'")
    Webpage = ""
    if request_data['Webpage']:
        BrandName = request_data['Webpage']
    customPrompt = " give me data in a json object format as same as above by adding new field GPTDecription , data should be a description rewrite by the prompte:   " + \
        " For each ad opportunity provided by our database, generate insights in less than 100 words on how the opportunity  " + \
        " aligns with the campaign objectives of our client, "+BrandName+". The output should focus solely on the name  " + \
        " of the ad opportunity and a concise insight that explains its strategic fit. Consider the client`s vision,  " + \
        " goals, and the specifics of their campaign, which can be inferred from their webpage "+Webpage+". The  " + \
        " insight should articulate:\n\n1. How the ad opportunity is suitable for the client`s campaign goals. " + \
        " \n2. The strategic value of the ad opportunity in the context of the client`s overall marketing strategy. " + \
        " \n3. Any specific aspect of the ad opportunity that particularly resonates with the client`s intended message  " + \
        " or brand positioning.\n\nThis tailored insight will help in demonstrating the relevance and potential impact  " + \
        " of each ad opportunity in achieving the client`s marketing objectives, ensuring the recommendations are both  " + \
        " strategic and aligned with the client`s brand vision. " + \
        " result should be in a JSON format, no other data should be included, NOTE: In GPTDecription if there any charater such as comma(,) it should be treated as a string "
    Prompt = json.dumps(mediaDataForPrompt)+customPrompt

    # return JsonResponse(Prompt, safe=False)
    response = generate_response(Prompt)
    responseData = response.choices[0].text
    responseData = responseData.replace(
        '\n\n\n\n', '')
    responseData = responseData.replace(
        '\n\n\n', '')
    responseData = responseData.replace(
        '\n\n', '')
    responseData = responseData.replace(
        '\n', '')
    # responseData = responseData.replace(
    #     '"{', '{')
    # responseData = responseData.replace(
    #     '}"', '}')
    responseData = responseData.replace(
        '\\', '')
    splitdata = responseData.split('[')
    if len(splitdata) > 1:
        splitdata = splitdata[1].split(']')
    else:
        splitdata = splitdata[0].split(']')
    finalData = "["+splitdata[0]+"]"
    rewritedData = finalData
    # rewritedData = rewritedData.replace(',', '-').replace('- \"', ', \"').replace('}- {', '}, {').replace("'", '`')

    # return JsonResponse(rewritedData, safe=False)
    # try:
    #     json_object = json.loads(rewritedData)
    #     return JsonResponse(json_object, safe=False)
    # except:
    #     return JsonResponse(rewritedData, safe=False)

    # # Print the JSON object
    # print("=====================================================================")
    # print(json_object)
    # print("=====================================================================")
    json_object = json.loads(rewritedData)
    finalData = []
    finalData.append(mediaDataAll)
    finalData.append(json_object)

    return JsonResponse(finalData, safe=False)


def remove_html_tags(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()
