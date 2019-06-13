from django.conf.urls import url
from api import views


urlpatterns = [
    url(r'^campaigns/$', views.campaigns_list),
    url(r'^campaigns/(?P<_id>[0-9]+)/$', views.campaigns_detail),
    url(r'^ad_groups/$', views.ad_groups_list),
    url(r'^ad_groups/(?P<_id>[0-9]+)/$', views.ad_groups_detail),
    url(r'^expanded_text_ad/$', views.expanded_list),
    url(r'^expanded_text_ad/(?P<ad_group_id>[0-9]+)/$', views.expanded_detail),
    ]
