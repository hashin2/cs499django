from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from cs499.cs499_app.views.api.views import display_session
from django.conf.urls.defaults import *

#******** Purpose ********#
# the urlpatterns below will call the associated function when the url pattertern appears

urlpatterns = patterns('',
    url(r'^api/', include('cs499.cs499_app.views.api.urls')),   
    (r'^login/$', 'cs499.cs499_app.views.api.views.login_view'),
    (r'^login/session/$', 'cs499.cs499_app.views.api.views.session_view'),
    (r'^login/session/account/', 'cs499.cs499_app.views.api.views.manageAccount'),   
    url(r'^login/session/(\d+)',  'cs499.cs499_app.views.api.views.display_session'),
    (r'^logout/', 'cs499.cs499_app.views.api.views.logout_view'),  
    (r'^register/$', 'cs499.cs499_app.views.api.views.register'),   
    url(r'^heatmap/',  'cs499.cs499_app.views.api.views.heatmap_view'),
    url(r'^login/session/heatmap(\d+)',  'cs499.cs499_app.views.api.views.display_heatmap'),
    url(r'^login/session/delete(\d+)',  'cs499.cs499_app.views.api.views.delete_session'),    
    (r'^login/session/app/', 'cs499.cs499_app.views.api.views.manageApps'),     
    (r'^login/session/device/', 'cs499.cs499_app.views.api.views.manageDevices'),   
    (r'^login/session/viewdevices/', 'cs499.cs499_app.views.api.views.viewdevices'), 
    (r'^login/session/viewapps/', 'cs499.cs499_app.views.api.views.viewapps'),        
)
