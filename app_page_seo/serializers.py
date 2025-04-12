from rest_framework import serializers
from .models import BoutiquePageSeo, PageSeo


class PageSeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageSeo
        fields = (
            'SortId',
            'PageSeoId',
            'PageName',
            'SEOMetaTitle',
            'SEOMetaDescription',
            'SEOMetaKeyword'
        )


class BoutiquePageSeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoutiquePageSeo
        fields = (
            'SortId',
            'BoutiquePageSeoId',
            'CountryId',
            'AudienceId',
            'SEOMetaTitle',
            'SEOMetaDescription',
            'SEOMetaKeyword'
        )
