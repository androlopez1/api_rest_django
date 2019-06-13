from django.db import models

# Create your models here.

class Campaigns(models.Model):
    
    PAUSED = 'PAUSED'
    ON = 'ON'
    DISPLAY = 'DISPLAY'
    SEARCH = 'SEARCH'

    STATUS_CHOICES = (
        (PAUSED, 'PAUSED'),
        (ON,'ON'),
        )

    CHANNEL_CHOICES = (
        (SEARCH, 'SEARCH'),
        (DISPLAY, 'DISPLAY'),
        )
    
        
    _id = models.IntegerField(default=1)
    name = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    budget = models.IntegerField(default=0) 
    advertising_channel_type = models.CharField(max_length=15, choices=CHANNEL_CHOICES)

class AdGroups(models.Model):

    ENABLED = 'ENABLED'
    OFFLINE = 'OFFLINE'

    STATUS_CHOICES = (
        (ENABLED,'ENABLED'),
        (OFFLINE, 'OFFLINE'),
        )
    
    _id = models.IntegerField(default=1)
    name = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    campaign_id = models.IntegerField(default=0)

class Expanded(models.Model):

    xsi_type = models.TextField()
    ad_group_id = models.IntegerField(default=1)
    headline_part1 = models.CharField(max_length=40)
    headline_part2 = models.TextField()
    description = models.TextField()
    path1 = models.TextField()
    path2=models.TextField()
    


