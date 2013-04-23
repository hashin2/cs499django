from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from cs499.cs499_app.views.api.views import display_session
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^api/', include('cs499.cs499_app.views.api.urls')),
    #url(r'^api/(?P<username>\d+)/viewFiles/$', 'api.viewFiles.viewSession') 
    #url(r'^login/$','cs499.cs499_app.views.api.auth.views.login_user'),
    # (r'^test/?$',
        # 'cs499.cs499_app.views.api.test.hello_world'),
    # (r'^login/', include(admin.site.urls)),
    (r'^base/', 'cs499.cs499_app.views.api.views.base'),
    # (r'^login/$', 'django.contrib.auth.views.login'),
    # (r'^accounts/login/', 'django.contrib.auth.views.session_view'),
    (r'^login/$', 'cs499.cs499_app.views.api.views.login_view'),
    (r'^login/session/$', 'cs499.cs499_app.views.api.views.session_view'),

    (r'^login/session/account/', 'cs499.cs499_app.views.api.views.manageAccount'),   

    url(r'^login/session/(\d+)',  'cs499.cs499_app.views.api.views.display_session'),
    (r'^logout/', 'cs499.cs499_app.views.api.views.logout_view'),
    # (r'^login/', 'django.contrib.auth.views.login'),
    # (r'^accounts/',include('registration.backends.default.urls')),
    # (r'^registerP/$', 'cs499.cs499_app.views.api.views.register'), 

    (r'^register/$', 'cs499.cs499_app.views.api.views.register'),  
    (r'^validate', 'cs499.cs499_app.views.api.views.validate'),        
   
    # (r'^accounts/login/?next=/session/', 'cs499.cs499_app.views.api.views.session_view'),
    # url(r'^authenticate/(?P<service>[a-z]+)/$', 'authenticate_redirect',name='authenticate_redirect'),
	# url(r'^authorize/callback/$', 'authorize_callback',	name='authorize_callback'),
)
