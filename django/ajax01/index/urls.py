''' ajax01/index/urls.py '''
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^01_xmlhttp/$', xmlhttp_views),
    url(r'^01_request/$', request01_views),
    url(r'^02_params/$', params_views),
    url(r'^02_request/$', request02_views),
    url(r'^03_post/$', post_views),
    url(r'^03_request/$',request03_views),
    url(r'^04_form/$',form_views),
    url(r'04_request/$',request04_views),
    url(r'05_checkname/$',checkname_views),
    url(r'05_request/$',request05_views),
    url(r'06_json/$',json_views),
    url(r'06_request/$',request06_views),
    url(r'07_json/$',json07_views),
    url(r'07_request/$',request07_views),
    url(r'08_request/$',request08_views),
    url(r'09_request/$',request09_views),
    url(r'^10_filter/$',filter_views),
]
