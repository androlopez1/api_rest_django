from rest_framework import serializers
from .models import Campaigns, AdGroups, Expanded

class CampaignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaigns
        fields = ('_id', 'name', 'status', 'budget', 'advertising_channel_type')

class AdGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdGroups
        fields = ('_id', 'name', 'status', 'campaign_id')

class ExpandedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expanded
        fields = ('xsi_type', 'ad_group_id', 'headline_part1','headline_part2', 'description', 'path1','path2')
