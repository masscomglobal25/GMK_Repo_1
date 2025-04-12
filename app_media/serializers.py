from rest_framework import serializers
from .models import CampaignReportDetail, CampaignReportRegister, Cart, EstimateShorten, Plan, PlanDetail


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = (
            # 'SortId',
            'CartId',
            'AdvertiserId',
            'MediaAdTypeId',
            'StartDate',
            'MediaLink',
            'MediaAdUnitLink',
            'CartStatus',
            'CartType',
            'MediaDetail',
            'MediaAdTypeDetail',
            'Vertical',
            'Amount',
        )


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = (
            # 'SortId',
            'PlanId',
            'AdvertiserId',
            'AdvertiserDetails',
            'CreatedByUserType',
            'CreatedByUserId',
            'PlanName',
            'BrandName',
            'BrandCategory',
            'CampaignObjective',
            'StartDate',
            'SourceFrom',
            'EstimateAmount',
            'Currency',
            'PlanCreatedDate',
            'PlanExpiryDate',
            'PaidExcelDownload',
            'Status',
            'AdvertiserAssistanceSupport',
            'AssistanceSupportCreditUsed'
        )


class ViewPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = (
            'SortId',
            'PlanId',
            'AdvertiserId',
            'AdvertiserDetails',
            'CreatedByUserType',
            'CreatedByUserId',
            'PlanName',
            'BrandName',
            'BrandCategory',
            'CampaignObjective',
            'StartDate',
            'SourceFrom',
            'EstimateAmount',
            'Currency',
            'Status',
            'Approval',
            'Payment',
            'Creative',
            'PlanCreatedDate',
            'PlanExpiryDate',
            'PaidExcelDownload',
            'CreativeDocFile',
            'AdvertiserAssistanceSupport',
            'AssistanceSupportCreditUsed'
        )


class PlanListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = (
            # 'SortId',
            'PlanId',
            'AdvertiserId',
            'AdvertiserDetails',
            'CreatedByUserType',
            'CreatedByUserId',
            'PlanName',
            'StartDate',
            'SourceFrom',
            'EstimateAmount',
            'PaidExcelDownload',
            'Currency',
            'Status',
            'Approval',
            'Payment',
            'Creative',
            'CreativeDocFile'
        )


class PlanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanDetail
        fields = (
            # 'SortId',
            'PlanDetailId',
            'PlanId',
            'AdvertiserId',
            'MediaAdTypeId',
            'StartDate',
            'MediaLink',
            'MediaAdUnitLink',
            'SourceFrom',
            'ExpiryDate',
            'MediaDetail',
            'MediaAdTypeDetail',
            'Vertical',
            'Amount',
            'CampaignUnit',
            'TotalServedCount',
            'Status',
        )


class EstimateShortenSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstimateShorten
        fields = (
            # 'SortId',
            'EstimateShortenId',
            'PlanId',
            'AdvertiserId',
            'PlanName',
        )


class CampaignReportRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignReportRegister
        fields = (
            'SortId',
            'CampaignReportRegisterId',
            'PlanId',
            'PlanDetailId',
            'ReportType',
            'StartDate',
            'EndDate',
            'UploadProof',
            'ProofLink'
        )

class SaveCampaignReportRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignReportRegister
        fields = (
            'CampaignReportRegisterId',
            'PlanId',
            'PlanDetailId',
            'ReportType',
            'StartDate',
            'EndDate',
            'ProofLink'
        )



class UploadCampaignReportRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignReportRegister
        fields = (
            'SortId',
            'CampaignReportRegisterId',
            'UploadProof',
        )


class CampaignReportDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignReportDetail
        fields = (
            'SortId',
            'CampaignReportDetailId',
            'CampaignReportRegisterId',
            'Unit',
            'OtherUnit',
            'ServedCount',
        )
