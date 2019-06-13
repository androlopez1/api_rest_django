from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Campaigns, AdGroups, Expanded
from api.serializers import CampaignsSerializer, AdGroupSerializer, ExpandedSerializer

# Create your views here.

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

###CAMPAIGNS###
@csrf_exempt
def campaigns_list(request):
    
    #list all campaigns, or create new one
    
    if request.method == 'GET':
        campaigns = Campaigns.objects.all()
        serializer = CampaignsSerializer(campaigns, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CampaignsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def campaigns_detail(request,_id):
    
    #retrieve, update or delete a campaign

    try:
        serie = Campaigns.objects.get(_id=_id)
    except Campaigns.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CampaignsSerializer(serie)
        return JSONResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CampaignsSerializer(serie, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        serie.delete()
        return HttpResponse(status=204)

###AD_GROUPS###
@csrf_exempt
def ad_groups_list(request):
    
    #list all ad_groups, or create new one
    
    if request.method == 'GET':
        groups = AdGroups.objects.all()
        serializer = AdGroupSerializer(groups, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AdGroupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

def ad_groups_detail(request,_id):
    
    #retrieve, update or delete a campaign

    try:
        serie = AdGroups.objects.get(_id=_id)
    except AdGroups.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AdGroupSerializer(serie)
        return JSONResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AdGroupSerializer(serie, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        serie.delete()
        return HttpResponse(status=204)

###EXPANDED_TEXT_AD###
@csrf_exempt
def expanded_list(request):
    
    #list all expandede text ad, or create new one
    
    if request.method == 'GET':
        expanded = Expanded.objects.all()
        serializer = ExpandedSerializer(expanded, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ExpandedSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def expanded_detail(request,ad_group_id):
    
    #retrieve, update or delete a expanded text ad

    try:
        serie = Expanded.objects.get(ad_group_id=ad_group_id)
    except Expanded.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ExpandedSerializer(serie)
        return JSONResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ExpandedSerializer(serie, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        serie.delete()
        return HttpResponse(status=204)
