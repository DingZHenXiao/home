"""index URL Configuration
"""
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^01_parent/$', parent_views),
    url(r'^02_child/$',child_views),
    url(r'^03_addauthor/$',addauthor_views),
    url(r'^04_publisher/$',addpublisher_views),
    url(r'^05_addbook/$',addbook_views),
    url(r'^06_query/$',query_views),
    url(r'^07_update',update_views),
    url(r'^08_delauthor/(\d+)$',delauthor_views,
        name="del"),
    url(r'^09_updateauthor/(\d+)$',
        updateauthor_views,name="update"),
    url(r'^10_doF/$',doF_views),
    url(r'^11_doQ/$',doQ_views),
    url(r'^12_oto/$',oto_views),
    url(r'^13_otm/$',otm_views),
    url(r'^14_mtm/$',mtm_views),
    url(r'^15_mtm/$',mtm1_views),
    url(r'^16_manager/$',manager_views),
    url(r'^17_manager/(\d+)$',manager1_views),
    url(r'^18_manager/(\S+)$',manager2_views),
    url(r'^19_update/$',update2_views),
]
