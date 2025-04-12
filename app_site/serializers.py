from rest_framework import serializers
from .models import CampaignPDFData, Comments, Log, PriorityCode, SiteSettings


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = (
            # 'SortId',
            'LogId',
            'Content',
            'UserType',
            'UserName',
            'UserId',
            'LogType',
            'JsonData',
            'CretedDate'
        )


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = (
            # 'SortId',
            'SiteSettingId',
            'DefaultCountry',
            'DefaultListingCountry',
            'DefaultListingVertical',
            'DefaultCurrency',
            'DefaultTimeZone',
            'DraftExpiryDays',
            'PaymentPendingExpiryDays',
            'DefaultAdvertiserCredits',
            'CreditsExpiryDays',
            'ExcelCredits',
            'Priority100Enable',
            'PlanItemDatePickerEnable',
            'UploadingImageSize',
            'UploadingAudioSize',
            'UploadingMediaKitSize',
            'FreeCreditOnRequest',
            'AdOpportunityPrompt',
            'MediaLocationPrompt',
            'NoOfOpportunitiesPerPlanEnterprise',
            'NoOfOpportunitiesPerPlanNormal',
            'VerticalSpecificCategoryOrder',
            'InitRedirectionLink'
        )


class CampaignPDFDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignPDFData
        fields = (
            # 'SortId',
            'PDFDataId',
            'UserId',
            'CampaignId',
            'PDFData'
        )


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = (
            # 'SortId',
            'CommentId',
            'FromId',
            'FromUserTypeId',
            'CommentType',
            'TypeId',
            'Comments',
            'CommentDate'
        )

class PriorityCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriorityCode
        fields = (
            # 'SortId',
            'PriorityCodeId',
            'PriorityCode'
        )

