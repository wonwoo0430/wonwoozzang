from django.conf.urls import url, include
from django.shortcuts import render, get_object_or_404
from . import views

urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^$',views.index, name = 'index'),
    url(r'^search/', include('haystack.urls')),

    url(r'^A/$',views.A, name = 'A'),
url(r'^AA/$',views.AA, name = 'AA'),
url(r'^AABA/$',views.AABA, name = 'AABA'),
url(r'^AAC/$',views.AAC, name = 'AAC'),
url(r'^AAL/$',views.AAL, name = 'AAL'),
url(r'^AAN/$',views.AAN, name = 'AAN'),
url(r'^AAOI/$',views.AAOI, name = 'AAOI'),
url(r'^AAON/$',views.AAON, name = 'AAON'),
url(r'^AAP/$',views.AAP, name = 'AAP'),
url(r'^AAPL/$',views.AAPL, name = 'AAPL'),
url(r'^AAWW/$',views.AAWW, name = 'AAWW'),
url(r'^AAXN/$',views.AAXN, name = 'AAXN'),

]
